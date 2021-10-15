import dis

board = [['_']*3 for i in range(3)]

print(board)
# Place a mark in row 1, column 2 and check the result
board[1][2] = 'X'
# print(board)
# print(dis.dis('s[a] += b'))
fruits = ['grape', 'raspberry', 'apple', 'banana']
# print(sorted(fruits, reverse=True))
print(sorted(fruits, key=len, reverse=True))
fruits.sort()
print(fruits)
