import sys
import re
import os
import urllib, urlparse

with open('salida') as f:
    for line in f:
        match = re.search('/bitstream/handle/(\d+)/(\d+)/', line)
        if match:
            directory = match.group(1) + "/" + match.group(2)
            if not os.path.exists(directory):
                os.makedirs(directory)
            print "Created directory:" + directory
        
            if re.search("l\d+", line):
                trozos = re.split(":", line)
                url = "https://addi.ehu.es" + trozos[1].replace("\"","").strip()[:-1]
                split = urlparse.urlsplit(url)
                filename = directory + "/" + split.path.split("/")[-1]
                if re.search("pdf", filename, re.IGNORECASE):
                    if not os.path.isfile(filename):
                        print "Download " + url + " to: " + filename
                        urllib.urlretrieve(url, filename)
                
f.closed
