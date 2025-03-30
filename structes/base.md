## Линейные структуры данных

### Стек
Стек &mdash; простая структура данных. В ней можно только удалять из конца и добавлять в конец.
Стек похож на упрощённый список.

```python
class Stack:
    def __init__(self):
        self.st1=[]
    def push(self, elem): self.st1.append(elem)
    def pop(self): return self.st1.pop()
    def top(self): return self.st1[-1]
    def size(self): return len(self.st1)
```

Стек нужен для например такой задачи:

**Скобки**

Вам дана строка s. В ней присутствуют символы : ( ) [ ] { }
Провертье является ли она правильной скобочной последовательностью?

*Решение:* а что если будем хранить стек открытых скобок, если попадает открытая мы её добавляем в стек, а елис закрывающия тогда проверяем а подходит ли она последний открытой скобки? если да тогда мы удаляем из стека элемент. Если нет то строка не является правильной скобочной последовательностью.

```python
def ok(s1, s2):
    if s1 == '(' and s2 == ')':
        return True
    elif s1 == '[' and s2 == ']':
        return True
    elif s1 == '{' and s2 == '}':
        return True
    return False

stack = Stack()
s = input()
for item in s:
    if item == '(':
        stack.append('(')
    elif item == '[':
        stack.append('[')
    elif item == '{':
        stack.append('{')
    else:
        if ok(stack.top(), item):
            stack.pop()
        else:
            print("NO")
            exit()
if stack.size() == 0:
    print("YES")
else:
    print("NO")
```

### Очередь
Очередь является структурой похитрее, добавляется элемент в конец, а удаляется из начала.
Очередь можно хранить как опять список, а потом удалять из начала но это долго. Можно ещё реализовать очередь с указателем на начало очереди. Но очередь через указатели может быть неудобной для задачи [Очередь с минимумом](#Очередь-с-минимумом) , 
А очередь можно разбить на 2 [стека](#Стек) : в первый стек мы всегда добавляем. А из второго удаляем. При этом если постпует запрос на удаление элемента а 2 стек пуст тогда мы переливаем первый стек во второй.
С помощью этой идеи, можно реализовать [очередь с минимумом](#Очередь-с-минимумом) .

```python
class Queue:
    def __init__(self):
        self.st1 = Stack()
        self.st2 = Stack()
    def push(self, elem):self.st1.push(elem)
    def pop(self):
        if self.st2.size() == 0:
            for _ in range(self.st1.size()):
                self.st2.push(self.st1.pop())
            return self.st2.pop()
        return self.st2.pop()
    def front(self):
        if self.st2.size() == 0:
            for _ in range(self.st1.size()):
                self.st2.push(self.st1.pop())
            return self.st2.top()
        return self.st2.top()
    def size(self): return self.st1.size() + self.st2.size()
```

###### Очередь с минимумом

Реализуете очердь с минимумом.
Для решения этой задачи нужно немножко подкоректировать класс:

```python
class Stack:
    def __init__(self):
        self.st1=[]
        self.mins =[]
    def push(self, elem):
        self.st1.append(elem)
        if elem < mins[-1]:
            self.mins.append(elem)
        else:
            self.mins.append(mins[-1])
    def pop(self):
        self.mins.pop()
        return self.st1.pop()
    def top(self): return self.st1[-1]
    def size(self): return len(self.st1)
    def getMin(self):
        return self.mins[-1]
    
class Queue:
    def __init__(self):
        self.st1 = Stack()
        self.st2 = Stack()
    def push(self, elem):self.st1.push(elem)
    def pop(self):
        if self.st2.size() == 0:
            for _ in range(self.st1.size()):
                self.st2.push(self.st1.pop())
            return self.st2.pop()
        return self.st2.pop()
    def front(self):
        if self.st2.size() == 0:
            for _ in range(self.st1.size()):
                self.st2.push(self.st1.pop())
            return self.st2.top()
        return self.st2.top()
    def size(self): return self.st1.size() + self.st2.size()
    def getMin(self):
        if self.st2.size() == 0:
            for _ in range(self.st1.size()):
                    self.st2.push(self.st1.pop())
                return self.st2.getMin()
        if self.st1.size() == 0:
            return self.st2.getMin()
        min1 = self.st1.getMin()
        min2 = self.st2.getMin()
        return min(min1, min2)
```

### Дек
Дек &mdash; это очередь с 2 концами. У неё можно удалять из конца, добавлять в начало, удалять из начала, добавить в конец.
В Python и в c++ есть встроенный дек. Но давайте поймём как его написать самим.
Дек можно реализовать через 2 стека : 1 &mdash; это первая половина дека, второй &mdash; втроая половинка.
Когда какой-то стек оказался пуст тогда из другого дека переливаем ровно половину элементов. И так делаем пока элементы не закончатся. Когда постпает запрос на удаление элемента из начала тогда берётся верхний элемент 2 стека. Иначе первого.
Дек реализуется так:


```python
class Stack:
    def __init__(self): self.stack = []
    def push(self, elem): self.stack.append(elem)
    def pop(self): return self.stack.pop()
    def top(self): return self.stack[-1]
    def size(self): return len(self.stack)

class Deque:
    def __init__(self):
        self.st1 = Stack()
        self.st2 = Stack()
        self.tmp = Stack()
    def push(self, elem):
        self.st2.push(elem)
    def pushfront(self, elem):
        self.st1.push(elem)
    def pop(self):
        if self.st2.size() > 0:
            return self.st2.pop()
        else:
            for _ in range(self.st1.size() // 2):
                self.tmp.push(self.st1.pop())
            for _ in range(self.st1.size()):
                self.st2.push(self.st1.pop())
            for i in range(self.tmp.size()):
                self.st1.push(self.tmp.pop())
            return self.st2.pop()
    def popfront(self):
        if self.st1.size() > 0:
            return self.st1.pop()
        else:
            for _ in range(self.st2.size() // 2):
                self.tmp.push(self.st2.pop())
            for _ in range(self.st2.size()):
                self.st1.push(self.st2.pop())
            for i in range(self.tmp.size()):
                self.st2.push(self.tmp.pop())
            return self.st1.pop()
    def size(self):
        return self.st1.size() + self.st2.size()
```

Задач на дек много приведём 1 из них:

**Деки**

Напишите программу, которая умеет оперировать большим количеством деков. Дек — это «очередь с двумя концами».

```python
class Stack:
    def __init__(self): self.stack = []
    def push(self, elem): self.stack.append(elem)
    def pop(self): return self.stack.pop()
    def top(self): return self.stack[-1]
    def size(self): return len(self.stack)

class Deque:
    def __init__(self):
        self.st1 = Stack()
        self.st2 = Stack()
        self.tmp = Stack()
    def push(self, elem):
        self.st2.push(elem)
    def pushfront(self, elem):
        self.st1.push(elem)
    def pop(self):
        if self.st2.size() > 0:
            return self.st2.pop()
        else:
            for _ in range(self.st1.size()//2):
                self.tmp.push(self.st1.pop())
            for _ in range(self.st1.size()):
                self.st2.push(self.st1.pop())
            for i in range(self.tmp.size()):
                self.st1.push(self.tmp.pop())
            return self.st2.pop()

    def popfront(self):
        if self.st1.size() > 0:
            return self.st1.pop()
        else:
            for _ in range(self.st2.size() // 2):
                self.tmp.push(self.st2.pop())
            for _ in range(self.st2.size()):
                self.st1.push(self.st2.pop())
            for i in range(self.tmp.size()):
                self.st2.push(self.tmp.pop())
            return self.st1.pop()
    def size(self):
        return self.st1.size() + self.st2.size()


n = int(input())
deques = {}
for i in range(n):
    indt = input().split()
    if indt[0] == 'pushfront':
        if indt[1] not in deques:
            deques[indt[1]] = Deque()
        deques[indt[1]].pushfront(indt[2])
    elif indt[0] == 'pushback':
        if indt[1] not in deques:
            deques[indt[1]] = Deque()
        deques[indt[1]].push(indt[2])
    elif indt[0] == 'popfront':
        print(deques[indt[1]].popfront())
    else:
        print(deques[indt[1]].pop())    
```

