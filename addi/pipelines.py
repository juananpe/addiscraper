# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy.orm import sessionmaker
from scrapy.exceptions import DropItem
from addi.models import Project, Link, db_connect, create_table
import logging

class AddiPipeline(object):
    def __init__(self):
        """
        Initializes database connection and sessionmaker
        Creates tables
        """
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)


    def process_item(self, item, spider):
        """Save projects in the database
        This method is called for every item pipeline component
        """
        session = self.Session()
        project = Project()
        link = Link()
        project.name = item["project"]
        project.date = item["date"]
        project.author = item["author"]
        project.repo = item["repo"]

        # check whether the author exists
        #exist_author = session.query(Author).filter_by(name = author.name).first()
        #if exist_author is not None:  # the current author exists
        #    quote.author = exist_author
        #else:
        #    quote.author = author

        # check whether the current quote has tags or not
        if "links" in item:
            for link in item["links"]:
                if not link.startswith('http'):
                    link = 'https://addi.ehu.es' + link
                link_obj = Link(url=link)
                # check whether the current tag already exists in the database
                # exist_tag = session.query(Tag).filter_by(name = tag.name).first()
                # if exist_tag is not None:  # the current tag exists
                #    tag = exist_tag
                project.links.append(link_obj)

        try:
            session.add(project)
            session.commit()

        except:
            session.rollback()
            raise

        finally:
            session.close()

        return item


class DuplicatesPipeline(object):

    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates tables.
        """
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)
        logging.info("****DuplicatesPipeline: database connected****")

    def process_item(self, item, spider):
        session = self.Session()
        exist_project = session.query(Project).filter_by(name = item["project"]).first()
        session.close()
        if exist_project is not None: 
            raise DropItem("Duplicate item found: %s" % item["project"])
        else:
            return item

