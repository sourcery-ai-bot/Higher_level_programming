#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 25 14:05:14 2020

@author: Robinson Montes
"""


class Rectangle:
    """class Rectangle that defines a rectangle figure

    Attributes:
        number_of_instances (int): Number of created rectangles
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Init method for Rectangle

        Attributes:
            width (int, optional): The width of the rectangle
            height (int, optional): The height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """
        str method to print rectangle

        Returns:
            string : The string with # rectangle
        """
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string

        for i in range(self.__height):
            for _ in range(self.__width):
                string += str(self.print_symbol)
            if i < self.__height - 1:
                string += '\n'
        return string

    def __repr__(self):
        """
        provides __repr__ method for object rectangle

        Returns:+
            string (str): string to get
        """
        return f"Rectangle({str(self.__width)}, {str(self.__height)})"

    def __del__(self):
        """
        delete method for rectangle
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def height(self):
        """
        Property height to retrieve it

        Returns:
            height (int): The height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter height of the rectangle

        Attributes:
            height (int): The height of the rectangle

        Raises:
            TypeError: If height is not an integer
            ValueError: If height is less than 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """
        Property width to retrieve it

        Returns:
            width (int): The width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter width of the rectangle

        Attributes:
            width (int): The width of the rectangle

        Raises:
            TypeError: If width is not an integer
            ValueError: If width is less than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        """
        Calculate the area of the rectangle

        Returns:
            The area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle

        Returns:
            The perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def bigger_or_equal(self, rect_2):
        """
        Method to compare 2 rectangles

        Attributes:
            rect_1 (class Rectangle): Rectangle 1 must be an instance rectangle
            rect_2 (class Rectangle): Rectangle 2 must be an instance rectangle

        Raises:
            TypeError: If rect_1 or rect_2 aren't instance of rectangle

        Returns:
            The biggest rectangle
        """
        if type(self) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_2 if rect_2.area() > self.area() else self

    @classmethod
    def square(cls, size=0):
        """
        Class method that defines a square

        Attributes:
            cls : The parameter that points to the class
            size (int): The size of the square

        Returns:
            width = height = size

        """
        return cls(size, size)
