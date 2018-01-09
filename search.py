class search():
    def __init__(self,bank,category,type):
        self.__bank=bank
        self.__category=category
        self.__type=type

    def get_bank(self):
        return self.__bank
    def get_category(self):
        return self.__category
    def get_type(self):
        return self.__type

    def set_bank(self,bank):
        self.__bank=bank
    def set_category(self,category):
        self.__category=category
    def set_type(self,type):
        self.__type=type