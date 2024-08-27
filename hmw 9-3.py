import random

num2 = [random.randint(-50, 50) for _ in range(20)]
print(num2)
# a
power_3 = list(map(lambda x: x**3, num2))
print(power_3)
# b
last_digit = list(map(lambda x: abs(x) % 10, num2))
print(last_digit)
# c
fahrenheit = list(map(lambda x: x * 9//5 + 32, num2))
print(fahrenheit)
# d
pos_neg = list(map(lambda x: "positive" if x > 0 else "negative", num2))
print(pos_neg)
# e
max_min = list(map(lambda x: "max" if x == max(num2) else "min" if x == min(num2) else x, num2))
print(max_min)
# f
reversed_num = list(map(lambda x: int(str(x)[::-1]) if x > 0 else -int(str(abs(x))[::-1]), num2))
print(reversed_num)
# g
abs_num = list(map(lambda x: abs(x), num2))
print(abs_num)
print()