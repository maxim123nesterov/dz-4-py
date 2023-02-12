# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.

# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18

# 6 12

n = int(input('Введите размер первого множества - '))
set1 = set()

for i in range(n):
    set1.add(input())

m = int(input('Введите размер второго множества - '))
set2 = set()
for i in range(m):
    set2.add(input())
print('Первое множество', set1)
print('Второе множество', set2)

intersection_set = set1.intersection(set2) 
print('Общее множество без повторений ', intersection_set)
list_1 = list(intersection_set)
for i in range(0, len(list_1)):
     for j in range(i+1, len(list_1)): 
        if(list_1[i] > list_1[j]): 
            temp = list_1[i]; 
            list_1[i] = list_1[j]; 
            list_1[j] = temp


print('Отсортированный список', list_1)



