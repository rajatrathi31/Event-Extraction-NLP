import xml.etree.ElementTree as ET
import os
import sys

file_path = sys.argv[1]
sentences = []
max_len = 0
i = 0
j = 0



for path, dirs, files in os.walk(file_path):
    for file in files:
        if(file.endswith(".xml")):
            root = ET.parse(os.path.join(file_path,file)).getroot()
            length = len(root.findall(".//W"))
            if(length>512) :
                i+=1
            j+=1
print(i,j)