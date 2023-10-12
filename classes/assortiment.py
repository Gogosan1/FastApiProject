class assortiment:
    # ассортимент для магазина
    def __init__(self, name, unit, number, best_before_date = "none"):
        self.__name = name
        self.__unit = unit
        self.__number = number
        self.__best_before_date = best_before_date
        
    def __init__(self, name, unit, number, purchase_price, provider, best_before_date = "none"):
        self.__name = name
        self.__unit = unit
        self.__number = number
        self.__purchase_price = purchase_price
        self.__provider = provider
        self.__best_before_date = best_before_date