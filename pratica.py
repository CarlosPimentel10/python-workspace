print(list(range(0, 5)))

# Accept multiple values


def get_sum2(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum


print(get_sum2(1, 2, 3, 4))

mariana = 2
renato = 4
larissa = 2
rafael = 5
augusto = 1
rafaela = 3

dedos = {mariana, renato, larissa, rafael, augusto, rafaela}
participantes = 6
somaDedos = sum(dedos)
dedoapontadorapara = 0

for x in range(somaDedos):
    if dedoapontadorapara > participantes:
        dedoapontadorapara = 0
    dedoapontadorapara += 1
dedos = list(dedos)

print('No final o dedo foi apontado para {}.'.format(
    dedos[dedoapontadorapara]))
