
a=1;#对a进行赋值

#下面一行是循环语句 while是python的关键字,表示循环
#while 右面是循环执行的条件,注意 循环条件右边要加冒号
while a>0:
    a= input("a=")
    a=int(a)
    print("@ a =",a);

#循环结束 注意下面的语句没有比while语句多了4个空格,这表示下面一条语句和while语句是顺序执行的
print("LOOP FIN")