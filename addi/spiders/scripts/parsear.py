import sys
import re
import os
import urllib, urlparse

with open('salida') as f:
    for line in f:
        if re.search("\"id", line):
            trozos = re.search('\d+', line)
            directory = trozos.group(0)
            if not os.path.exists(directory):
                os.makedirs(directory)
            print "Created directory:" + directory
        else:
            if re.search("linkdetail", line):
                trozos = re.split(":", line)
                url = "https://addi.ehu.es" + trozos[1].replace("\"","").strip()[:-1]
                split = urlparse.urlsplit(url)
                filename = directory + "/" + split.path.split("/")[-1]
                if re.search("pdf", filename, re.IGNORECASE):
                    if not os.path.isfile(filename):
                        print "Download " + url + " to: " + filename
                        urllib.urlretrieve(url, filename)
                
f.closed
