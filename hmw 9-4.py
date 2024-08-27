fruits = ["Mango", "Orange", "Banana", "Apple",
          "Strawberry", "Pineapple", "Grapes", "Watermelon"]
# a
reversed_fruit = list(map(lambda x: x[::-1], fruits))
print(reversed_fruit)
# b
first_letter = list(map(lambda x: x[:1], fruits))
print(first_letter)
# c
len_fruit = list(map(lambda x: len(x), fruits))
print(len_fruit)
# d
fruit_uppercase = list(map(lambda x: x.upper(), fruits))
print(fruit_uppercase)
# e
ends_with_s = list(map(lambda x: x + "!" if x.endswith("s") else x, fruits))
print(ends_with_s)