import  random

def init():
    global pc_choice
    a = ['石头','剪刀','布']
    pc_choice = random.choice(a)

def user():

    while True:
        if user_choice=='剪刀' or user_choice=='石头' or user_choice=='布':
            return  user_choice
            break
        else:
            print('您输入有误，请重新输入')
            continue
def pk():
    global user_choice
    init()
    user_choice = input('你的选择是：（石头/剪刀/布）')
    while True:
        if pc_choice == '剪刀':
            print('电脑出剪刀')
            if user()=='剪刀':
                print('你出的是剪刀，你两平手')
            elif user()=='石头':
                print('你出的是石头，你赢了')
            elif user()=='布':
                print('你出的是布，你输了')
            break
        elif pc_choice == '石头':
            print('电脑出石头')
            if user()=='剪刀':
                print('你出的是剪刀，你输了')
            elif user()=='石头':
                print('你出的是石头，你两平手')
            elif user()=='布':
                print('你出的是布，你赢了')
            break
        elif pc_choice == '布':
            print('电脑出布')
            if user()=='剪刀':
                print('你出的是剪刀，你赢了')
            elif user()=='石头':
                print('你出的是石头，你输了')
            elif user()=='布':
                print('你出的是布，你两平手')
            break

pk()


