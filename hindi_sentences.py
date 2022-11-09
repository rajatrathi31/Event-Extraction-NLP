import pandas as pd
import xml.etree.ElementTree as ET
import os

# sentences = []
# s = ""

# def extract(item) :
#     for child in item :
#         # print(child.tag)
#         if(child.tag == "P") :
#             if(len(s) != 0) :
#                 sentences.append(s)
#         elif(child.tag == "W"):
#             # s = s + " " + child.text
#             print(child.text)
#         else:
#             extract(child)
#     # sentences.append(s)

path = "hindi_ee/test/1-5-lac-property-ashes-in-a-fire-caused-by-short-circuit-hindi-news5.txt.xml"
tree = ET.parse(path)
root = tree.getroot()

# extract(root)

# print(sentences)

# for item in root.findall("P") :
# for j in root.findall("W") :
#     print(j.text)
# # print(root.findall("W"))

# for child in root :
#     print(child.attrib)

file_path = "./test"
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



            


