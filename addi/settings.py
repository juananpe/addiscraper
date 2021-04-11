# -*- coding: utf-8 -*-

# Scrapy settings for addi project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'addi'

SPIDER_MODULES = ['addi.spiders']
NEWSPIDER_MODULE = 'addi.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'addi (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'addi.middlewares.AddiSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'addi.middlewares.MyCustomDownloaderMiddleware': 543,
#}

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.httpcache.HttpCacheMiddleware': None,
    'scrapy_httpcache.downloadermiddlewares.httpcache.AsyncHttpCacheMiddleware': 900,
}



# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'addi.pipelines.AddiPipeline': 300,
#}

# ITEM_PIPELINES = {'addi.pipelines.MongoDBPipeline': 300, }

ITEM_PIPELINES = {
        'addi.pipelines.DuplicatesPipeline': 100, 
        'addi.pipelines.AddiPipeline': 200, 
        }

# MONGODB_SERVER = "localhost"
# MONGODB_PORT = 27017
# MONGODB_DB = "addi"
# MONGODB_COLLECTION = "tfgs"

# MySQL
CONNECTION_STRING = "{drivername}://{user}:{passwd}@{host}:{port}/{db_name}?charset=utf8".format(
     drivername="mysql",
     user="juanan",
     passwd="",
     host="localhost",
     port="3306",
     db_name="uam_projects",
)

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# -----------------------------------------------------------------------------
# SCRAPY HTTPCACHE SETTINGS
# -----------------------------------------------------------------------------
HTTPCACHE_ENABLED = True
HTTPCACHE_IGNORE_HTTP_CODES = [301, 302, 500, 503]
HTTPCACHE_STORAGE = 'scrapy_httpcache.extensions.httpcache_storage.MongoDBCacheStorage'
HTTPCACHE_MONGODB_HOST = '127.0.0.1'
HTTPCACHE_MONGODB_PORT = 27017
HTTPCACHE_MONGODB_USERNAME = ''
HTTPCACHE_MONGODB_PASSWORD = ''
HTTPCACHE_MONGODB_CONNECTION_POOL_KWARGS = {}
HTTPCACHE_MONGODB_AUTH_DB = 'admin'
HTTPCACHE_MONGODB_DB = 'cache_storage'
HTTPCACHE_MONGODB_COLL = 'cache'

