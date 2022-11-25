import xml.etree.ElementTree as ET
import os
import sys

file_path = sys.argv[1]
sentences = []

sf = open(sys.argv[2], 'w')
pf = open(sys.argv[3], 'w')

events = set()
args_type = set()

for path, dirs, files in os.walk(file_path):
    for file in files:
        if(file.endswith(".xml")):
            root = ET.parse(os.path.join(file_path,file)).getroot()
            for p in root.findall('P') :
                s = []
                for item in p.iter() :
                    if(item.tag == 'W') :
                        s.append(item.text)
                

                # pointer file
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
                            event_dict[item.attrib["ID"]] = [index, index+words-1, item.tag + ":" + (item.attrib["TYPE"] if item.attrib.get('TYPE')!=None else "NA")]
                            events.add(item.tag + ":" + (item.attrib["TYPE"] if item.attrib.get('TYPE')!=None else "NA"))
                            #print("Event : ", item.tag, index, index+words-1)
                        elif link!=None:
                            args_type.add(item.tag)
                            if(arg_dict.get(link.attrib["EVENT_ARG"])== None) :
                                arg_dict[link.attrib["EVENT_ARG"]] = [[index, index+words-1, item.tag]]
                            else :
                                arg_dict[link.attrib["EVENT_ARG"]].append([index, index+words-1, item.tag])
                            #print("Event Arg : ", item.tag, index, index+words-1)
                sys.stdout = pf
                for event in event_dict.items() :
                    if arg_dict.get(event[0]) == None :
                        print(*event[1],1,1,"NA",sep = ' ', end = ' | ')
                        continue
                    for args in arg_dict.get(event[0]) :
                        print(*event[1], *args, sep= ' ', end = ' | ')
                if len(event_dict) :
                    print()

                if len(event_dict):
                    sf.write("<unknown> <unknown>")
                    sf.write(' '.join(s))
                    sf.write('\n')


sf.close()
pf.close()

with open('event_type.txt', 'w') as f:
    for item in events:
        f.write(item + '\n')

with open('arg_type.txt', 'w') as f:
    for item in args_type:
        f.write(item + '\n')
