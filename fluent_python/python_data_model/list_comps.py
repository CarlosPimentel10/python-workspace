symbols = '$¢£¥€¤'
# iterative way
'''
code = []
for symbol in symbols:
    code.append(ord(symbol))

print(code)
'''
# list comps
code = [ord(symbol) for symbol in symbols]
# print(code)
numbers = [x for x in range(1, 11)]

# print(numbers)
# list comps vs map and filter
# beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
# print(beyond_ascii)
beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
print(beyond_ascii)
# cartesian products using list comps
colors = ['black', 'white', 'yellow']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors
           for size in sizes]
print(tshirts)
