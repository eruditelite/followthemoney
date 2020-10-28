import sys
import xml.etree.ElementTree as ET

if (2 != len(sys.argv)):
    print("Usage: ", str(sys.argv[0]), " <xml file>")
    sys.exit(1)

tree = ET.parse(str(sys.argv[1]))
root = tree.getroot()

print("contributor\tamount")

for records in tree.findall('records'):
    for record in records.findall('record'):
        contributor = record.find('Contributor').text
        amount = record.find('Amount').text
        print(contributor, "\t", amount)
