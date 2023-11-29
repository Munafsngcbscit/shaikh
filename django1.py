num=10
a,b=0,1
print(a,b,end=" ")
for i in range(num):
        c=a + b
        a = b
        b = c
        print(c,end=" ")
print()

# def fib(n):
#     a = 0
#     b = 1
#     if n == 1:
#         print(a)
#     else:
#         print(a)
#         print(b)
#         for i in range(2,n):
#             c = a + b
#             a = b
#             b = c
#             print(c)
# fib(10)
# write a python program that generate the first 10 number in the fibonacci sequence ?
# a = int(input('enter a no: '))
# def fib(n):
#     a, b = 0, 1
#     for i in range(n):
#         yield a
#         a, b = b, a + b
# print (list(fib(a)))