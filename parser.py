from bs4 import BeautifulSoup

with open("list.xml") as file:
    src = file.read()
soup = BeautifulSoup(src, "xml")
for tag in soup.find_all('atom:title'):
    if tag.text == 'Document_КартыЛПАБ_КатегорииРеакцийРаботника':
        xml_file = open(f'{tag.text}.xml', "w+")
        xml_file.close()
# with open('input.xml', encoding="utf-8") as fd: 
#     lines = fd.readlines()
#     for line in lines:
#         if line.strip()[:7] == "<entry>":
#             with open('Document_КартыЛПАБ_КатегорииРеакцийРаботника.xml', "w", encoding="utf-8") as file:
#                 file.write(line.strip() + '\n')
#         if line.strip()[:8] == "</entry>":
#             with open('Document_КартыЛПАБ_КатегорииРеакцийРаботника.xml', "a", encoding="utf-8") as file:
#                 file.write(line.strip())
with open('input.xml', 'r') as f:
	file_from_read = f.read() 
sp = BeautifulSoup(file_from_read, 'xml')
tags = sp.find_all('feed')
with open('Document_КартыЛПАБ_КатегорииРеакцийРаботника.xml', "w", encoding="utf-8") as file_to_write:
    for tg in tags:
        file_to_write.write(str(tg))
