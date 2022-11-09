import pandas as pd
import xml.etree.ElementTree as ET
import os

file_path = "./hindi_ee/train"
sentences = []

with open("output.txt", "w") as f:

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



            


