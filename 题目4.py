"""
输入一个正整数m(20<=m<=100)，计算 11+12+13+...+m 的值。

输入格式:
在一行输入一个正整数m。

输出格式:
在一行中按照格式“sum = S”输出对应的和S.

输入样例:
在这里给出一组输入。例如：

90
输出样例:
在这里给出相应的输出。例如：

sum = 4040
"""
def fun(m):
    if m>11:
       return fun(m-1)+m
    else :
       return m
while True:
    m=int(input())
    if 20<=m<=100:
        break
    else:
        print("请重新输入：")
        continue
print(fun(m))