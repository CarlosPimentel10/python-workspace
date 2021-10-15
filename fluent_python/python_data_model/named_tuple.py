# Defining and using a named tuple type
from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)
print(tokyo.population)
# namedtuples methods
print(City._fields)
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
# _make() lets you instantiate a named tuple from an iterable;
# City(*delhi_data) would do the same
delhi = City._make(delhi_data)
# _asdict() returns a collections.OrderedDict built from the named tuple
# instance. That can be used to produce a nice display of city data
# print(delhi._asdict())
for k, v in delhi._asdict().items():
    print(k + ':', v)
