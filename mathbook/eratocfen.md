### Решето Эратосфена
Решето Эратосфена это  поиск простых чисел от числа $а$ до числа $b$.
Сначала мы вычеркиваем все числа которые делятся на 2, потом 
которые делятся на 3, потом которое делятся на 5, и.д. В результате 
останутся только одни простые числа.

И для этого мы сделаем такую реализацию:

```python
a, b = (int(y) for y in input().split())
primes = []
s = a
for i in range(a, b+1):
    div = 2
    flag = True
    while div*div <= i:
        if i % div == 0:
            flag = False
            break
        div += 1
    if flag == True:
        primes.append(i)

print(*primes)
```
