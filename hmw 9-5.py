cities = ["Tokyo", "New York", "Paris", "London", "Sydney", "Dubai", "Shanghai"]
print(cities)
# a
sorted_len = sorted(cities, key=lambda x: len(x))
print(sorted_len)
# b
sorted_last_letter = sorted(cities, key=lambda x: x[-1])
print(sorted_last_letter)
# c
sorted_by_reverse = sorted(cities, key=lambda x: x[::-1])
print(sorted_by_reverse)


