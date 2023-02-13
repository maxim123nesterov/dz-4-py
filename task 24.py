n = int(input('Введите размер куста - '))
a = list(map(int, input('Сколько ягод растет на кусте - ').split()))

max = 0

for i in range(n):
	cursum = sum(a[i:i+3])
	if cursum > max:
		max = cursum
if a[0] + a[-1] + a[-2] > max:
	max = a[0] + a[-1] + a[-2]
if a[0] + a[1] + a[-1] > max:
	max = a[0] + a[1] + a[-1]

print(max)