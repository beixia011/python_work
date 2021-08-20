#This rensapp is used to login rensapp
#Must remember this app is going to remix 
#thank you for your use

print('rensapp_login系统')
print('版本号：v1.01.1001')
print('感谢使用')

users={}
user=input('请输入你的账号')

while user not in users:
    print('你还未注册，请注册后重新登录')
    new_user=input()
    new_user_password=input()
    new_user_password_regret=input()
    if new_user_password != new_user_password_regret:
        print('两次密码不一样哦，再试一次')
    else:
        print('恭喜注册成功，接下来去注册吧')
        new_user=user 
        users[user]=new_user_password
        break

print('请输入你的账号')
login={}


while True:
    login_user=input()
    if login_user not in users:
        print('你是不是账号输入错了，再看看啦')
    else:
        login_password=input()
    login[login_user]=login_password
    if login[login_user]==users[user]:
        print(f'欢迎回来，{login_user}')
        break
    else:
        print('是不是密码错了，再检查检查')

input()
