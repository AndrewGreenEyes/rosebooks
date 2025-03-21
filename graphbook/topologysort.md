### Алгоритм Дейкстры


Алгоритм Дейкстры находит кратчайшие расстояние между вершинами но **только во взешанных графах** . Кратчайшие расстояние это минимальный вес между вершинами.
Алгоритм Дейкстры можно поставить в другую сторону чтобы он находил максимальный вес который нужно потратить между 2 вершинами.

> Алгоритм Дейкстры работает только на графах где все веса неотрицательны

Алгоритм Дейкстры похож на Обход в ширину.

Реализация номер 1:

```python
import collections as coll
def dijkstra(start):
    dist = [float('inf')] * (n+1)
    dist[start] = 0
    q = coll.deque()
    q.append(start)
    while len(q):
        vertex = q.popleft()
        for v, w in graph[vertex]:
            newd = dist[vertex] + w
            if newd < dist[v]:
                dist[v] = newd
                q.append(v)
    return dist
    
```

Реализация:

```python
from collections import deque as Queue
from heapq import *

def dijkstra(start):
    dist = [float('inf')] * (n+1)
    st = []
    dist[start] = 0
    heappush(st, (0, start))
    while st:
        saved_dist, v = heappop(st)
        if saved_dist != dist[v]:
            continue
        for vertex, wes in graph[v]:
            new_d = dist[v] + wes
            if dist[vertex] == float('inf') or new_d < dist[vertex]:
                dist[vertex] = new_d
                heappush(st, (dist[vertex], vertex))
    return dist
```

#### Востановление ответа
Чтобы востановить ответ в Дейкстре нужно добавить некоторые строчки о создании списка родителя:

```python
import collections as coll
def dijkstra(start):
    parent = [0] * (n+1)
    dist = [float('inf')] * (n+1)
    dist[start] = 0
    q = coll.deque()
    q.append(start)
    while len(q):
        vertex = q.popleft()
        for v, w in graph[vertex]:
            newd = dist[vertex] + w
            if newd < dist[v]:
                dist[v] = newd
                q.append(v)
                parent[v] = vertex
    return dist, parent


```

А потом для востановления ответа нужно пройтись по списку родителя так как было и в обходе в ширину.

