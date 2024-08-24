
import random
number = random.randint(3, 20)
print(number, '- ', end='')
result = []
for i in range(1, 20):
    for j in range(1, 20):
        if (number % (i + j) == 0) and (i < j):
            result.append(i)
            result.append(j)

for i in range(len(result)):
    print(result[i], end='')




