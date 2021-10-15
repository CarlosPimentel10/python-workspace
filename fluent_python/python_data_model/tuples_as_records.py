"""Examples of tuples used as records"""
lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokio', 2003, 32450, 0.66, 8014)
traveler_ids = [
    ('USA', '31195855'),
    ('BRA', 'CE342567'),
    ('ESP', 'XDA205856'),
]

for passport in traveler_ids:
    print('%s/%s' % passport)

# tuple unpacking
for country, _ in traveler_ids:
    print(country)
# another example of unpacking
latitude, longitude = lax_coordinates
print(latitude)
print(longitude)
print(divmod(20, 8))
t = (20, 8)
quotient, remainder = (divmod(*t))
print(divmod(*t))
print(quotient)
print(remainder)
