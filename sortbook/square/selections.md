## Сортировка выбором
Сортировка выбором основывается на поисках минимального элемента. Например если был список:
	5 3 4 9 1 2 7 6 8
то сортировка выбором найдёт сначала минимальный элемент — 1, потом следующий минимальный — 2, и т. д.
Реализация:
Замечание: используете первую реализацию с встроенной функцией min потому что она быстрее.

1. Первая реализация

```python
def select_sort(liston):
    result = []
    for i in range(len(liston)):
        r = min(liston)
        ind = liston.index(r)
        liston.pop(ind)
        result.append(r)
    return result
```

2. Вторая реализация

```python
def select_sort(liston):
    #result = []
    size = len(liston)
    for i in range(size):
        imin = 0
        for j in range(i+1, size):
            if liston[j] < liston[imin]:
                imin = j
        liston[i], liston[imin] = liston[imin], liston[i]
    return liston
```

