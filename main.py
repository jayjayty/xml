import xml.etree.ElementTree as ET
mytree = ET.parse('zaebal2.xml')
myroot = mytree.getroot()
print(myroot)