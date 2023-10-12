from helper_classes.address import address
from helper_classes.full_name import full_name
from helper_classes.pasport import pasport

class worker:
    #конструктор для создания работника для бухгалтерии
    def __init__(self, full_name, address, pasport,Inn, snils, wage): 
        self.__full_name = full_name
        self.__address = address
        self.__pasport = pasport
        self.__Inn = Inn
        self.__sinls = snils
        self.__wage = wage
        