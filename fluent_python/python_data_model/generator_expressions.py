import array


symbols = '$¢£¥€¤'
list_of_symbols = tuple(ord(symbol) for symbol in symbols)
print(list_of_symbols)
list_array = array.array('I', (ord(symbol) for symbol in symbols))
print(list_array)
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)
