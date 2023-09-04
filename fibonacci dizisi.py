a=0
b=1
fibonacci_dizisi=[a,b]
for i in range(10):
    a,b=b,a+b
    fibonacci_dizisi.append(b)
print(fibonacci_dizisi)