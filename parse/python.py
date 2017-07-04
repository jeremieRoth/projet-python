import xml.etree.ElementTree as ET
tree = ET.parse('dbpedia_2015-10.nt')
root=tree.getroot()
print(root)