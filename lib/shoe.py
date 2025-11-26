#!/usr/bin/env python3
class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if isinstance(value, str):
            self._brand = value
        else:
            print("brand must be a string")

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            # ✔ TEST EXPECTS PRINT, NOT ERROR
            print("size must be an integer")

    def cobble(self):
        # ✔ EXACT STRING REQUIRED BY TEST
        print("Your shoe is as good as new!")
        self.condition = "New"
