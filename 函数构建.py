#函数的定义语法
"""
def 函数名（参数）
    函数体
    return（返回值）
参数和返回值可省略
\n表示换行
"""
def add(x,y):
    result=x+y
    print(f"{x}+{y}={result}")
    return(result)
a=add(1,5)
print(a)
#传入参数可不使用，也可以多个参数
num=float(input("shuo:"))
def check(num): 
    if num<37.5:
        print("hao")
    else:
        print("buhao")
check(num)

#函数返回值
#return后面的不执行
#none类型
def say_hi():
    print("nihao")
    return None
++result=say_hi()
#NONE在if语句中等同于false
def check_age(age):
    if age>18:
        return "sucess"
    else:
        return None
result=check_age(7)
if not result:
    print("you are not allowed")

#函数的嵌套调用
#变量的作用域
#局部变量：定义在函数体内部的范围
#全局变量：在函数内外均能使用，在外定义的变量
#global关键词：
num=100
def test_a():
    print(num)
def test_b():
    global num#声明该变量为全局变量
    num=100
    print(num)
test_a()
test_b()
print(num)
#综合运用
#控制台：详见第五章1-1

#定义全局变量
money=500000
name=None
#要求客户输入姓名
name=input("请输入你的姓名：")
#定义查询函数
def query(show_header):
    if show_header:#传参默认是True,=if True
        print("-----查询余额-----")
    print(f"{name},您的余额为：{money}元")
#定义存款函数
def saving(num):
    global money
    money=money+num
    print("-----存款-----")
    print(f"{name},您存款{num}元成功")
    #调用query
    query(False)
#定义取钱
def get_money(num):
    global money
    money-=num
    print("-----取款-----")
    print(f"{name},您取款款{num}元成功")
    query(False)
#定义主菜单函数
def main():
    print("-----主菜单-----")
    print(f"{name},欢迎来到ATM，请操作：")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")#\t制表符进行对齐
    return input("请输入你的选择：")
#无限循环
while True:
    keyboard_input=main()
    if keyboard_input=="1":
        query(True)
        continue#结束本次循环进入主菜单，进行下一次循环
    elif keyboard_input=="2":
        num=int(input("您想要存多少钱，请输入："))
        saving(num)
        continue
    elif keyboard_input=="3":
        num=int(input("您想要取多少钱，请输入："))
        get_money(num)
        continue
    else:
        print("程序退出")
        break#退出循环






