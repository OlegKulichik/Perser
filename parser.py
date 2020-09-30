import re


class Pars:

    def __init__ (self, file_name: str):
        self.file_name = file_name
    
    def read_file(self):
        with open(self.file_name, "r",) as file:
            result = file.read()
        return result

    def pars_text(self):
        meta = re.findall(r"\<[a-zA-Z]+.*?\>|\</[a-zA-Z]+.*?\>", self.read_file())
        return meta
        



pt = Pars("myfin.txt")
print(pt.pars_text())
