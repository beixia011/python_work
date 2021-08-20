print('欢迎使用ren编写的计算机')
print('本计算机基于python编写，感谢您的使用')
print('对滴，这就是一个简简单单的计算机')
print('下面开始使用吧')

print('开始选择您的计算方法咯')
print("加法输入'+',减法输入'j',乘法输入'c',除法滴话就输入'除法'吧,嘿嘿")
way=input()

while way=='+':
    print("你选择了加法哦，想退出就输入'quit'就可以啦")
    first_name=input('第一位数:')
    if first_name=='quit':
        break
    second_name=input('第二位数:')
    if second_name=='quit':
        break
    answer1 = int(first_name)+int(second_name)
    print('这个数的结果是:'+str(answer1))

while way=='j':
    print("你选择了减法哦，想退出就输入'quit'就可以啦")
    first_name=input('被减数：')
    if first_name=='quit':
        break
    second_name=input('减数：')
    if second_name=='quit':
        break
    answer2 = int(first_name)-int(second_name)
    print('这个数的结果是：'+str(answer2))


print("啊？你不想使用了吗")
input('那好吧，按任意键退出登录程序哦')
