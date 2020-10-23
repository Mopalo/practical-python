# bounce.py
#
# Exercise 1.5
height = 100
howMany = 1
bounceHeight = 3/5

while howMany < 11:
    bounceBack = height * bounceHeight
    print("Bounce number:", howMany, "Height:", round(bounceBack, 4)
    height = bounceBack
    howMany = howMany + 1
