import xml.etree.ElementTree as ET
import os
import sys

file_path = sys.argv[1]

event_dict = {}
arg_dict = {}


for path, dirs, files in os.walk(file_path):
        for file in files:
            if(file.endswith(".xml")):
                root = ET.parse(os.path.join(file_path,file)).getroot()
                for p in root.findall('P') :
                    event_dict = {}
                    arg_dict = {}
                    index = 2
                    for item in p.iter() :
                        if (item.tag == 'W') :
                            index += 1
                        elif (item.tag not in ['LINK','P','EVENT-COREF-LINK']) :
                            words = len(item.findall('.//W'))
                            link = item.find('LINK')
                            if ((link) == None) and item.attrib.get("ID")!=None :
                                event_dict[item.attrib["ID"]] = [index, index+words-1, item.tag , (item.attrib["TYPE"] if item.attrib.get('TYPE')!=None else "NA")]
                                #print("Event : ", item.tag, index, index+words-1)
                            elif link!=None:
                                if(arg_dict.get(link.attrib["EVENT_ARG"])== None) :
                                    arg_dict[link.attrib["EVENT_ARG"]] = [[index, index+words-1, item.tag]]
                                else :
                                    arg_dict[link.attrib["EVENT_ARG"]].append([index, index+words-1, item.tag])
                                #print("Event Arg : ", item.tag, index, index+words-1)
                    
                    for event in event_dict.items() :
                        if arg_dict.get(event[0]) == None :
                            print(*event[1],1,1,"NA",sep = ' ', end = ' | ')
                            continue
                        for args in arg_dict.get(event[0]) :
                            print(*event[1], *args, sep= ' ', end = ' | ')
                        #print(event[1],arg_dict.get(event[0]))

                    print()




   