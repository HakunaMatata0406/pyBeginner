"""
Write a Python program to print the following string in a specific format

Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high,
Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" Output :

Twinkle, twinkle, little star,
	How I wonder what you are!
		Up above the world so high,
		Like a diamond in the sky.
Twinkle, twinkle, little star,
	How I wonder what you are
"""

print("Twinkle, twinkle, little star, \n\tHow I wonder what you are!\n\t\t Up above "
      "the world so high,\n\t\t Like a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are")

"""
Write a Python program to get the Python version you are using
"""

import sys

python_version = sys.version
print("The python version is: ",python_version)
python_version_info = sys.version_info
print("The python version info is: ",python_version_info)

"""
Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14
"""

import datetime

current_date = datetime.datetime.now()
print("The Current date is : ", current_date.strftime("%Y-%M-%H %H:%M:%S"))

"""
Write a Python program which accepts the radius of a circle from the user and compute the area.

Sample Output :
r = 1.1
Area = 3.8013271108436504
"""

import math
# Method 1

radius = 1.1
area_of_circle = math.pi*radius*radius
print("The Area of the Circle is : ", area_of_circle)

# Method 2

circle_radius = int(input("Enter the radius: "))
area_of_circle = math.pi*circle_radius*circle_radius
print("The Are of the Circle is : ", area_of_circle)

# Method 3
