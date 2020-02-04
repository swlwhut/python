   # A = [91,95,97,99]
    #B = [92,93,96,98]
    #e = 0
    #c = A + B
    #d = len(A)+len(B)

    #for h in range(d):
    #    for i in range(d-1):
    #        if c[i]>c[i+1]:
    #            e = c[i]
    #            c[i] = c[i+1]
    #            c[i+1] = e
    #       else:
    #            continue
    #print(c)
#------------------------------------------------------
list1 =  [91, 95, 97, 99]
list2 =  [92, 93, 96, 98]

# 把 A 组成绩赋值给一个新列表，用来存合并的成绩——这个细节要注意！
list3 =list1
list3.extend(list2)
print(list3)

list3.sort(reverse=True)
print(list3)

#可通过索引提取元组中的某个元素-----------------
import random
appetizer = ['话梅花生','拍黄瓜','凉拌三丝']
def coupon(money):
    if money < 5:
        a = random.choice(appetizer)
        return a
    elif 5 < money < 10:
        b = random.choice (appetizer)
        return b, '溏心蛋'

result = coupon(6)
# result是一个元组
print(result[0])
print(result[1])
#-------------------------------------------------


#另外一种方式：我们也可以同时定义多个变量，来接收元组中的多个元素
import random
appetizer = ['话梅花生','拍黄瓜','凉拌三丝']
def coupon(money):
    if money < 5:
        a = random.choice(appetizer)
        return a
    elif 5 < money <10:
        b = random.choice (appetizer)
        return b, '溏心蛋'

dish, egg = coupon (7)
# 元组的两个元素分别赋值给变量dish和egg
print(dish)
print(egg)