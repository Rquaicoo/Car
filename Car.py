class Car:
    def __init__(self, year_model, make, speed=0):
        self.__year_model = year_model
        self.__make = make
        self.__speed = speed
    
    def accelerate(self):
        self.__speed = self.__speed + 5
        return self.__speed

    def brake(self):
        self.__speed = self.__speed - 5

        return self.__speed

    def get_speed(self):
        return self.__speed




