
# def salary_sum(name,time):
#     global a,b
#
#     a = time
#     b = name
#   a = int(input('该员工工作时长为'))
    # if a<6:
    #     print(b + '来了%d个月，奖金为500元' %a)
    # elif a>=6 and a<=12:
    #     print(b + '来了%d个月，奖金为%d元' %(a ,120*a))
    # else:
    #     print(b + '来了%d个月，奖金为%d' %(a , 180*a))
#
#

# 人力计算 注意：.ceil()是向上取整
# import math
# def estimated_number(size,time):
#     number = math.ceil(size * 80 / time)
#     print('项目大小为%.1f个标准项目，如果需要在%.1f个工时完成，则需要人力数量为：%d人' %(size,time,number))


import math

def estimated(size,number=None,time=None):
    if (number == None) and (time != None):
        number = math.ceil(size * 80 / time)
        print('项目大小为%.1f个标准项目，如果需要在%.1f个工时完成，则需要人力数量为：%d人' %(size,time,number))
    elif (number != None) and (time == None):
        time = size * 80 / number
        print('项目大小为%.1f个标准项目，使用%d个人力完成，则需要工时数量为：%.1f个' %(size,number,time))

a = int(input('请选择计算类型：（1-人力计算，2-工时计算）'))
if a == 1:
    print('您已选择人力计算')
    b = int(input('请输入项目大小：（1代表标准大小，可以输入小数）'))
    d = int(input('请输入工时数量'))
    estimated(b,None,d)
elif a == 2:
    print('您已选择工时计算')
    b = int(input('请输入项目大小：（1代表标准大小，可以输入小数）'))
    c = int(input('请输入人力数量：（请输入整数）'))
    estimated(b,c,None)





'请输入项目大小：（1代表标准大小，可以输入小数）'
'请输入人力数量：（请输入整数）'
'请输入工时数量：（请输入小数）'



















