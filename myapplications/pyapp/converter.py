from turtle import *
import math
def lener(ch, e1, e2):
    if e1==e2:return ch
    if e1 == 'km':
        if e2 == 'mm':return ch * 1000 * 100 * 10
        elif e2 == 'cm':return ch * 1000 * 100
        elif e2 == 'm':return ch * 1000
        else:return ch
    elif e1 == 'm':
        if e2 == 'mm':return ch * 100 * 10
        elif e2 == 'cm':return ch * 100
        elif e2 == 'km':return ch / 1000
        else:return ch
    elif e1 == 'cm':
        if e2 == 'mm':return ch * 10
        elif e2 == 'm':return ch / 100
        elif e2 == 'km':return ch / 100 / 1000
        else:return ch
    elif e1 == 'mm':
        if e2 == 'cm':return ch / 10
        elif e2 == 'm':return ch / 1000
        elif e2 == 'km':return ch / 1000 / 1000
        else:return ch
def timer(ch, e1, e2):
    if e1==e2:return ch
    if e1 == 'year':
        if e2 == 'mont':return ch * 12
        elif e2 == 'day':return ch * 365
        elif e2 == 'ned':return ch * 52
        elif e2 == 'h': return ch * 365 * 24
        elif e2 =='min':return ch * 365 * 24 * 60
        elif e2 == 'sec':return ch * 365 *24 * 60 * 60
        else:return 'INF'
    elif e1 == 'mont':
        if e2 == 'year':return ch / 12
        elif e2 == 'day':return ch * 30
        elif e2 == 'ned':return ch * 5
        elif e2 == 'h': return ch * 30 * 24
        elif e2 =='min':return ch * 30 * 24 * 60
        elif e2 == 'sec': return ch * 30 * 24 * 60 * 60
        else:return 'INF'
    elif e1 == 'day':
        if e2 == 'mont':return ch / 30
        elif e2 == 'ned':return ch / 7
        elif e2 == 'year':return ch / 365
        elif e2 == 'h':return ch * 24
        elif e2 == 'min':return ch * 24 * 60
        elif e2 == 'sec':return ch * 24 * 60 * 60
        else:return 'INF'
    elif e1 == 'h':
        if e2 == 'year':return ch / 24 / 365
        elif e2 == 'mont':return ch / 24 / 30
        elif e2 == 'ned':return ch / 24 / 7
        elif e2 == 'min':return ch * 60
        elif e2 == 'sec':return ch * 60 * 60
        else:return 'INF'
    elif e1 == 'min':
        if e2 == 'year':return ch / 60 / 24 / 365
        elif e2 == 'mont':return ch / 60 / 24 / 30
        if e2 == 'ned':return ch / 60 / 24 / 7
        elif e2 == 'day':return ch / 60 / 24
        elif e2 == 'h':return ch / 60
        elif e2 == 'min':return ch
        elif e2 == 'sec':return ch * 60
        else:return 'INF'
    elif e1 == 'sec':
        if e2 == 'ned':return ch / 60 /  60 / 24 / 7
        elif e2 == 'day':return ch / 60 / 60 / 24
        elif e2 == 'h': return ch / 60 / 60
        elif e2 == 'min': return ch / 60
        elif e2 == 'sec':return ch
        else: return 'INF'
def temperature(ch, e1, e2):
    if e1 == 'C':
        if e2 == 'K': return ch + 273.7
        else:return ch
    else:
        if e2 == 'C': return ch - 273.7
        else:return ch
def massa(ch, e1, e2):
    if e1 == e2:return ch
    if e1 == 't':
        if e2 == 'c':return ch * 10
        elif e2 == 'kg': return ch * 1000
        elif e2 == 'g':  return ch * 1000 * 1_000
        else: return 'inf'
    elif e1 == 'c':
        if e2 == 't': return ch / 10
        elif e2 == 'kg': return ch * 100
        elif e2 == 'g' : return ch * 100 * 1_000
        elif e2 == 'mg': return ch * 100 * 1_000 * 1000
        else: return 'inf'
    elif e1 == 'kg':
        if e2 == 't': return ch / 1000
        elif e2 == 'c': return ch / 100
        elif e2 == 'g': return ch * 1000
        elif e2 == 'mg':return ch * 1000 * 1000
    elif e1 == 'g':
        if e2 == 't':
            return ch / 1000 / 1000
        elif e2== 'c':
            return ch / 1000 / 100
        elif e2=='kg':return ch / 1000
        elif e2=='mg':return ch * 1000
    elif e1 == 'mg':
        if e2 == 'kg':
            r = ch / 1000
            return r / 1000
        elif e2 == 'g':
            r = ch / 1000
            return r
def angledraw(angle=-90):
    title("Рисуем углы")
    if angle == -90:
        angle = int(numinput("Угол", "Укажите угол (градусы):", minval=0, maxval=720))
    speed(90)
    angle%=360
    tt = "Прямой"
    if angle < 90:tt = "Острый"
    elif 90 < angle < 180:tt = "Тупой"
    elif angle == 180: tt = "Развёрнутый"
    elif angle == 360: tt = "Полный"
    else: tt = "Обратный угол"
    hideturtle()
    pencolor("violet")
    left(180)
    pensize(4)
    forward(150)
    right(180-angle)
    forward(150)
    up()
    goto(-140, -160)
    down()
    pencolor("black")
    write(f"Угол:{str(angle)} \nТип:{tt}", font="Arial 18")
    exitonclick()
def squares(ch, e1, e2):
    if e1 == e2:return ch
    if e1 == 'km':
        if e2 == 'm': return ch * (1000**2)
        elif e2 == 'cm': return ch * (1000**3)
        else:return 'inf'
    elif e1 == 'm':
        if e2 == 'km': return ch / (10**6)
        elif e2 == 'cm': return ch * 10000
        else: return 'inf'
    elif e1 == 'cm':
        if e2 == 'km': return ch / (10**9)
        elif e2 == 'm': return ch / 10_000
def objom(ch, e1, e2):
    if e1==e2:return ch
    if e1 == 'm':
        if e2 == 'cm': return ch * (10**6)
        elif e2 == 'dm': return ch * 1000
        else: return 'inf'
    elif e1 == 'dm':
        if e2 == 'm': return ch / 1000
        elif e2 == 'cm': return ch * 1000
        else: return 'inf'
    elif e1 == 'cm':
        if e2 == 'm': return ch / 1000
        elif e2 == 'dm': return ch / (10**6)
        else: return 'inf'
def systemischisl(ch, e1, e2):
    if e1 == e2: return ch
    alph = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    if e2 == '10':
        return int(str(ch), base=int(e1))
    mods = []
    n = ch
    while n > 0:
        mods.append(alph[n%int(e2)])
        n //=int(e2)
    return ''.join(mods[::-1])
def anglesser(ch, e1, e2):
    if e1==e2:return ch
    if e1 == 'g':
        if e2 == 'r':
            return ch / 57.2957795
    else:
        if e2 == 'g':
            return ch * 57.2957795

def speeder(ch, e1, e2):
    if e1 == 'km/h':
        if e2 == 'km/min':
            return ch * 60
        elif e2 == 'm/h':
            return ch * 1000
        elif e2 == 'm/min':
            return ch * 1000 // 60
    elif e1 == 'km/min':
        if e2 == 'km/h':
            return ch / 60
        elif e2 == 'm/h':
            return 'error'
    return 'error'


def comb(n, k):
    """
    Вы числить количество коминаторных сочетаний из N по K
    :return: C(n, k)
    """
    r = 1
    for i in range(min(k, n - k)):
        r = r * (n - i) // (i + 1)
    return r
def combmod(n, k, mod):
    """
    Вычислить количество комбинаторных сочетаний по модулю
    """
    m = min(k, n - k)
    r = [1] * (m + 1)
    res = m + 1
    for i in range(2, m + 1):
        res = res * (m + i) % mod
        r[i] = (mod - (mod // i) * r[mod % i] % mod) % mod
        res = res * r[i] % mod
    return res
def comb2(n, k):
    return comb(n+k, k)
def comb3(n, k):
    return factorial(n)//factorial(n-k)
def polinomyalcoofeceents(n, *a):
    a = list(a)
    if sum(a) != n:
        return -1
    res = factorial(n)
    for item in a:
        res //= factorial(item)
    return res
def catalan(n):
    return comb(2*n, n) - comb(2*n, n-1)
def gcd(integers):
    """
    НОД чисел
    :return: GCD(integers)
    """
    gcd = integers[0]
    for i in range(len(integers)):
        nod2 = integers[i]
        gcd = math.gcd(gcd, nod2)
    return gcd
def lcm(integers):
    lcm1 = integers[0]
    tabs = 1
    for i in range(len(integers)):
        nod2 = integers[i]
        lcm1 = lcm1 * nod2 // math.gcd(lcm1, nod2)
    return lcm1
def factorial(n):
    if type(n) == int:
        return math.factorial(n)
    else:
        return (n / math.e)**n * math.sqrt(2*math.pi*n)
