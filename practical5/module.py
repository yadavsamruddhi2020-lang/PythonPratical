# In Python, the 3 common types of modules you should know are:

# Built-in module → already provided by Python
# User-defined module → created by you
# External/third-party module → installed using pip

# built in module 

# square and power
# import math 
# num=25
# sq=math.sqrt((num))
# power=math.pow(2, 3)
# print(sq)
# print(power)


# random
# import random
# num=random.randint(1,10)
# print(num)

# date time
# import datetime
# today=datetime.datetime.now()
# print(today)


# os module 
# import os

# print("Current directory:")
# print(os.getcwd())


# user defined module 
# # addition
# def add(a,b):
#     return a+b

# # sq
# def sq(a):
#     return a*a

# # even odd
# def evenodd(a):
#     if a%2==0:
#         return "even"
#     else:
#         return "odd"


# def maximum(a, b):
#     if a > b:
#         return a
#     else:
#         return b


# third party module 

# numpy

# import numpy as np
# arr = np.array([10, 20, 30, 40])
# print("Sum =", np.sum(arr))
# print("Maximum =", np.max(arr))


# panda

# import pandas as pd
# data = {
#     "Name": ["A", "B", "C"],
#     "Marks": [80, 90, 75]
# }
# df = pd.DataFrame(data)
# print(df)




