# using lambdas
nums = [3, 2, 3, 4, 5, 6, 8, 9, 10, 14, 16, 19]

evens = list(filter(lambda n: n % 2 == 0, nums))

print(evens)
