#1 输出如下图案
'''
****
****
****
****
'''
row=1  #从第一行开始
while row < 5: #一共打印四行
    column = 1  #每一行都从第一列开始打印
    while column < 5:  #一共打印四列
        print('*' , sep='' , end='') #改变默认间隔和结尾换行
        column += 1
    print('')  # 打完一行要换行 打印内容为空 作用是换行
    row += 1
else:
    print('打印完毕')

#2 输出如下图案
'''
*
**
***
****
*****
'''
row2 = 1  #从第一行开始打印
while row2 < 6:  #一共打印五行
    column2 = 1   #每行都是从第一列开始打印
    while column2 <= row2 : #每一列打印数量上限是行数
        print('*' , sep='' , end='')
        column2+=1   #打印下一列
    print('')  #一行打印完要换行
    row2+=1  # 改变变量
else:
    print('打印完毕')

#3 输出如下内容：
'''
*****
****
***
**
*
'''
row3 = 1
while row3 < 6:
    column3 = 1
    while column3 <= 6-row3 :
        print('*' , sep='', end='')
        column3+=1
    print('')
    row3 += 1
else:
    print('打印完毕')

#4 输出如下内容
'''
   *
  ***
 *****
*******
'''
row4=1
while row4 < 5 :
    column4_blank = 1 #空格从第一列开始打印
    while column4_blank <= (8-2*row4)/2 : #最后一行是七个星星
        print(' ',sep='',end='')
        column4_blank += 1
    column4_star = 1 # 星星从空格打印完开始打印
    while column4_star <= 2*row4-1 :
        print('*',sep='',end='')
        column4_star += 1
    print('')
    row4 += 1
else:
    print('打印完毕')

#5 输出如下图案
'''
   *
  ***
 *****
*******
 *****
  ***
   *
'''
row5 = 1
while row5 < 8:
    if row5 <= 4:
        column5_blank = 1
        while column5_blank <= (8-2*row5)/2 : #最多一行是七个星星
            print(' ',sep='',end='')
            column5_blank += 1
        column5_star = 1  # 星星从空格打印完开始打印
        while column5_star <= 2 * row5 - 1:
            print('*', sep='', end='')
            column5_star += 1
        print('')
        row5 += 1
    if row5 > 4 :
        column5_blank = 1
        while column5_blank <= row5-4 :
            print(' ', sep='', end='')
            column5_blank += 1
        column5_star = 1
        while column5_star <= 7-2*(row5-4) :
            print('*', sep='', end='')
            column5_star += 1
        print('')
        row5 += 1
else:
    print('打印完毕')
