import random

numbers = [random.randint(1, 100) for _ in range(50)]
print(numbers)
# a
bigger_50 = list(filter(lambda x: x > 50, numbers))
print(bigger_50)
# b
divided_7 = list(filter(lambda x: not x % 7, numbers))
print(divided_7)
# c
bigger_10 = list(filter(lambda x: x > 9, numbers))
print(bigger_10)
# d
same_digit = list(filter(lambda x: x > 10 and not x % 11, numbers))
print(same_digit)
# e
digit_sum_9 = list(filter(lambda x: not x % 9, numbers))
print(digit_sum_9)
# f
bigger_avg = list(filter(lambda x: x > (sum(numbers)//len(numbers)), numbers))
print(bigger_avg)
# g
bigger_half = list(filter(lambda x: x > max(numbers)/2, numbers))
print(bigger_half)
# h
sorted_numbers = sorted(numbers)
sorted_first_half = sorted_numbers[len(numbers)//2]
bigger_sorted_first_half = list(filter(lambda x: x > sorted_first_half, numbers))
print(bigger_sorted_first_half)
# i
user_num = [int(input("enter a number")) for i in range(5)]
not_same = list(filter(lambda x: x not in user_num, numbers))
print(not_same)
# j
def prime_num(a):
    if a <= 1:
        return False
    for i in range(2, a-1):
        if not a % i:
            return False
    return True
a_prime = list(filter(lambda x: prime_num(x), numbers))
print(a_prime)
print()





