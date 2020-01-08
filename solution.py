# Solution for Metric Tree :-

# This is a explanatory solution

import re
import xml.etree.ElementTree as ET
import xmltodict
import json

# def to screen xml file
def screenXML(file):
    tree = ET.parse(file)
    root = tree.getroot()

    # get xml extention if any
    xmlMeta = re.match(r"\{(.+)\}.+", root.tag)

    if xmlMeta:
        xml = "{"+xmlMeta.group(1)+"}"

    # screens the patient name
    for patient in root.iter(xml + 'recordTarget'):
        for name in patient.iter(xml + 'name'):
            for nameValue in name.iter():
                if nameValue.tag != (xml + 'name'):
                    if nameValue.tag == (xml + 'family'):
                        nameValue.text = 'patient family name'
                    else : nameValue.text = 'patient name'

    # screen all the address
    for child in root.iter():
        if child.tag == (xml + 'addr'):
            for address in child.iter():
                if address.tag != (xml + 'addr'):
                    address.text = 'address'

    tree.write('solution.xml')


# def to manually convert xml to json
def xml2json(file):
    with open(file) as in_file:
        xml = in_file.read()
        with open('solution.json', 'w') as out_file:
            json.dump(xmltodict.parse(xml), out_file)
        

if __name__ == "__main__" :

    # Change file name here
    fileName = 'sample.xml'
    
    screenXML(fileName)
    print("XML screening completed. Screened file can be found in solution.xml")
    xml2json('solution.xml')
    print("Json convertion completed. Json file can be found in solution.json")
