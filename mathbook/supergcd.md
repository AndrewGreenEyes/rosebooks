Расширенный алгоритм Евклида

Рассмотрим следующее уравнение:

$ax+by=c$, где a, b и c — целые числа, a≥0, b≥0. Гарантируется, что a≠0 или b≠0. Необходимо найти все пары целых чисел x и y
, которые являются решением уравнения.

Пусть $d=gcd(a,b)$
. Если c не делится на d, то уравнение не имеет решений.

Рассмотрим уравнение: ax0+by0=d

Пусть мы нашли решение для уравнения $bx1+(a%b)y1=d$

Данное уравнение можно переписать в виде: $bx1+(a−⌊ab⌋b)y1=d$

Отсюда $ay1+b(x1−⌊ab⌋y1)=d$

Следовательно x0=y1
y0=x1−⌊ab⌋y1

Таким образом, получаем соотношения для рекурсивного алгоритма поиска решения уравнения. Такой алгоритм называется расширенным алгоритмом Евклида.

Рекурсия в этом алгоритме будет прекращаться в тот момент, когда b=0, так же, как и в обычном алгоритме Евклида.
Заметим, что алгоритм найдёт только одно решение уравнения — $x[0]$ и $y[0]$. Все остальные подходящие пары x и y связаны следующим свойством: x=x0+bdt y=y0−adt, где t
— любое целое число. Вернёмся к изначальному уравнению ax+by=c. Пусть x0 и y0 — решение уравнения ax0+by0=d, тогда x=cdx0+bdt y=cdy0−adt, где t— любое целое число

Реализация расширенного алгоритма Евклида

```python
def gcd_ext(a, b):
    if b == 0:
        return a, 1, 0
    d, x, y = gcd_ext(b, a % b)
    x, y = y, x - (a // b) * y
```
    return d, x, y
