# bounce.py
#
# Exercise 1.5


height = 100

for i in range(10):
    height = height * (3/5)
    print(i+1, round(height, 4))
    i = i + 1
    
