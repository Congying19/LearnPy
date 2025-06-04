number=eval(input('请输入您的6位中奖号码：'))
if number==987654:
    print("恭喜您中奖了！")

if number!=987654:
    print('您未能中奖')

n=98
if n%2 :
    print(n,'是奇数')
else:
    print(n,'是偶数')

print('是奇数'if n%2 else '是偶数')

socre=eval(input('请输入您的成绩：'))
if socre<0 or socre>100:
    print('成绩有误')
elif 60<=socre<=70:
    print('D')
elif 70<socre<=80:
    print('C')
elif 80<socre<=90:
    print('B')
elif 90<socre<=100:
    print('A')
else:
    print("E")

