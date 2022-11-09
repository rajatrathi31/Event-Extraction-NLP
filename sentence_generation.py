import xml.etree.ElementTree as ET
import os
import sys

file_path = sys.argv[1]
sentences = []

with open(sys.argv[2], "w") as f:

    for path, dirs, files in os.walk(file_path):
        for file in files:
            if(file.endswith(".xml")):
                root = ET.parse(os.path.join(file_path,file)).getroot()
                for p in root.findall('P') :
                    s = []
                    for item in p.iter() :
                        if(item.tag == 'W') :
                            s.append(item.text)
                    f.write(' '.join(s))
                    f.write('\n')



            


