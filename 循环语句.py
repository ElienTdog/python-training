#while 循环：while 条件
i=1
he=0
while i<=100:
    he=he+i
    i+=1
print(he)
#设置1-100的随机整数变量，while+input判断是否才对数字
import random
num=random.randint(1,100)
guess_num=int(input("请输入你猜测的数字："))
i=1
while guess_num!=num:
    if guess_num>num:
        print("大了")
    else:
        print("小了")
    guess_num=int(input("请再次输入你猜测的数字："))
    i+=1
print(f"恭喜你猜对了，你一共猜测了{i}次")

count=0
flag=True
while flag:
    guess_num=int(input("请输入你猜测的数字："))
    count+=1
    if guess_num==num:
        print("猜对了")
        flag=False
    else:
        if guess_num>num:
            print("大了")
        else:
            print("小了")
print(f"你总共猜了{count}次")

print("hello",end='')#输出不换行
print("hello\tworld")#\t制表符，对后面的对齐
#打印99乘法表-while循环
i=1
while i<=9:
    j=1
    while j<=i:
        print(f"{j}*{i}={j*i}\t",end='')
        j+=1
    i+=1
    print()
#for循环