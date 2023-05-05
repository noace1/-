from denglu import First
from win import Win
from tools import Text_mysql


if __name__ == '__main__':

    user = First().denglu()
    if user:
        print(user)
        text01 = Win(user)
        text02 = text01.kuang()
        #globals(xx)

    else:
        print('登录失败')
