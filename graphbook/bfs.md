### Обход в ширину

Обход в ширину находит кратчайшие растояния от одной вершины до всех других.

Обход в ширину можно представить как горящую сетку. Загорелась одна вершина все загорелисть через минуту, потом их соседние ещё через минуту и далее...

Обход в ширину напоминает обход в глубину. Но вместо стека там используется очередь.
Обход в глубину помогает найти количество рёбер которые нужно пройти от стартовой вершины до какой-то другой.
Алгоритм обхода в ширину:

```python
from collections import deque as Queue
def bfs(start):
    dist = [float('inf')] * (n+1)
    dist[start] = 0
    q = Queue()
    q.append(start)
    while len(q):
        v = q.popleft()
        for vertex in graph[v]:
            if dist[vertex] == float('inf'):
                dist[vertex] = dist[v] + 1
                q.append(vertex)
    return dist
```

> Обход в ширину используется на невзешанных графах.

*Коментарий: на взешанных графах используется алгоритм Дейкстры*

##### Дополнительные коментарии к обходу в ширину

1. Обход в ширину можно использовать для выеления компонет связанности.
2. Асимптотика обхода в ширину почти O(n + m)

#### Востановление пути

Теперь мы хотим не только знать минимальное число рёбер между вершинами s и t. Но ещё и сам путь.
Для этого для каждой вершины заведём ещё один список предков - т.е вершин из которых мы пришли в вершину x. У стартовой вершины её предок будет она сама.  Затем мы пойдем от вершины t по её предкам. От его - к его предкам и т.д. пока не дойдём до стартовой вершины.

*Коментарий к реализации: для быстродействия и улучшения памяти будем хранить ответ (расстояние и предки) в словаре. Например так {<вершина>:{'dist':<рассстояние>, 'parent':<предок>}}* 

```python
from collections import deque as Queue
def bfs(start):
    # dist = [float('inf')] * (n+1)
    # dist[start] = 0
    vertexes = {i+1:{"dist":float('inf'), "parent":-1} for i in range(n)}
    vertexes[start]["dist"] = 0
    vertexes[start]["parent"] = start
    q = Queue()
    q.append(start)
    while len(q):
        vertex = q.popleft()
        for v in graph[vertex]:
            if vertexes[v]["dist"] == float('inf'):
                q.append(v)
                vertexes[v]["dist"] = vertexes[vertex]["dist"] + 1
                vertexes[v]["parent"] = vertex
    return vertexes

n = 7
# задание графа списками смежности, стартовой конечных вершин...
result = bfs(start)
answer = []
current = finish
while current != start:
    answer.append(current)
    current = result[current]["parent"]
print(len(answer))
print(*answer[::-1])
```
