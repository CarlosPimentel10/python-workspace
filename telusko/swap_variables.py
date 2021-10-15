a = 5
b = 6

# 1. using a temp variable
# temp = a
# a = b
# b = temp
# 2. using xor
a = a ^ b
b = a ^ b
a = a ^ b

# 3. pythonic way
# a, b = b, a
# using arithmetic
# a = a + b
# b = a - b
# a = a - b
print(a)
print(b)
