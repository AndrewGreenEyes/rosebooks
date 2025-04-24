#  Динамическое программирование
Динамическое программирование строится по реккурентным соотношениям.
## Кузнечик
На числовой прямой стоит кузнечик - стоит в точке 0. Кузнечик может прыгнуть на 1, 2, 3, ... , к клеток вперёд. Сколькими
способами он может попасть в клетку  N?

```python
n, k= map(int, input().split())
ls = [1]
#jskdfjklasljfdkasjdddsfhakzjhdsfjaz
for i in range(1, n):
    if i < k:
        ls.append(sum(ls[:i]))
    else:
        ls.append(sum(ls[i-k:i]))
print(ls[-1])
```

## Заяц
Теперь заяц стоит на числовой прямой теперь в каждой клетке есть какое-то число морковок. Заяц прыгает на 1,2,3,...,к клеток вперёд. Какое максимальное
количество морковок он может принести в дом, если его дом находится в точке N?
Заяц не может прыгат назад

```python
n, k = map(int, input().split())
price = [0, 0]
price.extend(map(int, input().split()))
price.append(0)
c = [0] * (n+1)
pathPosishion = [1, 1]

for i in range(2, n+1):
    previos = c.index(max(c[max(1, i - k):i]), max(1, i - k), i)
    pathPosishion.append(previos)
    c[i] = max(c[max(1, i - k):i]) + price[i]
print(c[-1])
path = []
path.append(str(n))
Index = n
while Index > 1:
    i = pathPosishion[Index]
    Index = i
    path.append(str(Index))

print(len(path)-1)
print(" ".join(path[::-1]))
```

## Черепаха

Черепаха оказалась на клетчатой доске размером n*m в точке (1, 1). Каждым ходом она может сдвинуться только на клетку вправо либо только на клетку вниз.
Сколкими способами она может дойти в точку (n, m)?

```python
n, m = map(int, input().split())
ls = [[0]*m for i in range(n)]
ls[0][0] = 1
for i in range(n):
    for j in range(m):
        if i == j == 0:continue
        elif i == 0:
            ls[i][j] = ls[i][j-1]
        elif j == 0:
            ls[i][j] = ls[i-1][j]
        else:
            ls[i][j] = ls[i-1][j] + ls[i][j-1]
print(ls[-1][-1])

```

## Панда

Панда оказалась на доске размера n*m в клетке (1, 1). Каждым ходом она сдивигается только на клетку вправо либо только на клетку вниз.
В каждой клетке доски находится какое-то количество бамбука. Какое максимальное количество бамбука она сможет донести до своего дома, если её дом находится в 
клетке (n, m)?

```python
n, m = (int(I) for I in input().split())
cen = []
c = [[-100] * (m+1) for utdjijdsifa in range(n+1)]
for inputtt in range(n):
    cen.append([int(x) for x in input().split()])
c[0][0] = 0
c[0][1] = 0
c[1][0] = 0
pathposishion = []
path = []
for i in range(1, n+1):
    for j in range(1, m+1):
        c[i][j] = max(c[i-1][j] , c[i][j-1]) + cen[i-1][j-1]

print(c[-1][-1])
```
