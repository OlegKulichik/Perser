import re


class Pars:

    def __init__ (self, file_name: str):
        self.file_name = file_name
    
    def read_file(self):
        with open(self.file_name, "r",) as file:
            result = file.read()
        return result

    def find(self):
        meta = re.findall(r"<{}.*?{}=['']*.*?>".format(self.tag_name,self.attr),self.read_file())
        meta1 = re.findall(r"<{}.*?{}=['']*{}=['']*.*?>".format(self.tag_name,self.attr, self.attr1),self.read_file())
        return meta, meta1

    def set_tag_name(self, tag_name: str, attr: str = None, attr1: str = None):
        self.tag_name = tag_name
        self.attr = attr
        self.attr1 = attr1


pt = Pars("myfin.txt")
pt.set_tag_name("meta", "charset")
print(pt.find())
pt.set_tag_name("meta", "name","content")
print(pt.find())
