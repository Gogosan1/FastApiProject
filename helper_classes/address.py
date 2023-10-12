class address:
    def __init__(self, country, region, city, district, street, house, post_index, apartament = "none"):
        self.__country = country
        self.__region = region
        self.__city = city
        self.__district = district
        self.__street = street
        self.__house = house
        self.__post_index = post_index
        self.__apartament = apartament