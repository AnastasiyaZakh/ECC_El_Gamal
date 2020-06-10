import numpy as np
import matplotlib.pyplot as plt
from algorithms import cipolla_y
# from algorithms import cipolla_y
# y = lambda x: np.sin(x)
x = list(range(200))
# y = list(map(lambda x: cipolla_y.cipolla(x**3+1*x+6, 11), x))
y = list(map(lambda x: cipolla_y.cipolla(x**3-7*x+10, 127), x))

dic = dict(zip(x, y))
dicti = dict(dic)
for i in dic.keys():
	if dic[i] == 'Немає розв*язку':
		dicti.pop(i)
x = list()
y = list()
num = 0
for k, v in dicti.items():
	x.append(k)
	y.append(v)
	num += 1
print(num)
print(x, y)
# for y_i in y:
# 	if y_i == y[0]:
# 		y_sovpal = y_i
# 		print(y_i, "repeated")
for _ in range(8, len(y)):
	# print(y[_], _)
	_1 = 7
	_2 = 8
	_3 = 9
	if y[_] == y[_1] and y[_+1] == y[_2] and y[_+2] == y[_3]:
		print(_ - _1, "elements")
		print(_, y[_], y[_+1], y[_+2])
		print(y[_1], y[_2], y[_3])
		break

fig = plt.subplots()

plt.scatter(x, y)
plt.show()
