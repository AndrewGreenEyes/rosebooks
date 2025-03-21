### Обход в глубину
Пусть у нас будет граф:
Зададим его списком смежности:

```graph
type: not orient

1 : [2, 3, 4]
2 : [1, 3]
3 : [1, 2, 4]
4 : [1, 3]
```

Продемонстрируем обход в глубину:

Сначала создадим стек. Добави в стек стартувую вершину - 1. Пометим её посещёной. Теперь посмотрим исходящие из неё рёбра. Это ребра 2, 3, 4 все мы их добавим в стек.
Смотрим стек это вершина 4. Исходящие из неё ребра это вершина 1. Но так как она посещена то пропускаем вершину, следующая вершина это 3 но она уже в стеке не добавляем стек. 
Смотрим следующую вершина стека - эть вершина 3. ...

**Реализация**

*Коментарий:у обхода в глубину есть 2 реализации.*

```python
# Реализация с рекурсией

def dfs(start):
    visited[start] = 1
    for v in graph[start]:
        if not visited[v]:
            dfs(v)
```

```python
#  Нерекурсивная реализация

def dfs(start):
    stack = [start]
    while len(stack):
        vertex = stack.pop()
        visited[vertex] = 1
        for v in graph[start]:
            if not visited[v]:
                stack.append(v)
    
```

### Что помогает сделать обход в глубину?

**Компонеты связанности**

Дан граф заданый списком рёбер. Выведете все компоненты связанности в нём.

*Решение:*

```python
def dfs(start):
    stack = [start]
    s = set()
    while len(stack):
        vertex = stack.pop()
        visited[vertex] = 1
        s.add(vertex)
        for v in graph[start]:
            if not visited[v]:
                stack.append(v)
    return s
n, m = map(int, input().split())
graph = {i+1:[] for i in range(n)}
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
visited = [0] * (n+1)
for start in range(1, n+1):
    if not visited[start]:
        r = dfs(start)
        print(len(r))
        print(*sorted(list(r)))
```


