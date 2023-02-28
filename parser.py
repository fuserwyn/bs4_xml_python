from bs4 import BeautifulSoup

with open("list.xml") as file:
    src = file.read()
soup = BeautifulSoup(src, "xml")
for tag in soup.find_all('atom:title'):
    if tag.text == 'Document_КартыЛПАБ_КатегорииРеакцийРаботника':
        xml_file = open(f'{tag.text}.xml', "w+")
        xml_file.close()

with open('input.xml', 'r') as f:
    file_from_read = f.read() 
sp = BeautifulSoup(file_from_read, 'xml')
tag_names = ["d:Ref_Key", "d:LineNumber", "d:Категория_Key", "d:КатегорияВыбрана"]
entry = sp.find('entry')
for tg in tag_names:
    entry.append(sp.new_tag(tg, text='_NONE_'))
with open('Document_КартыЛПАБ_КатегорииРеакцийРаботника.xml', "w", encoding="utf-8") as file_to_write:
    file_to_write.write(str(sp))