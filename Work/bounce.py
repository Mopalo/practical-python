# bounce.py
#
# Exercise 1.5
height = 100
howMany = 1
bounceHeight = 3/5

while howMany < 5:
    bounceBack = height * bounceHeight
    print("Bounce number:", howMany, "Height:", bounceBack)
    height = bounceBack
    howMany = howMany + 1
