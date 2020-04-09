#Base64
text=input('请输入3的倍数位字符串：')
if len(text)%3==0:#判断字符长度是否为三的倍数
    code2=''#对应二进制位
    code64=''#对应Base64编码
    Base64='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'#对应索引到Base64编码的键值对
    for i in text:#此循环用于获得text的完整二进制位code2
        ASCII=bin(ord(i))[2:]#将字符转化成整数，再转化成二进制数，并去除前缀0b
        add0=8-len(ASCII)
        code2+=add0*'0'+ASCII#补全二进制数八位所空缺的零
    for j in range(len(code2)//6):#此循环将code2以6为间隔分割，并转化成十进制对应的Base64编码的键，按照键生成值
        code64+=Base64[int(code2[j*6:j*6+6],2)]
    print(code64)
else:
    print('输入错误！')
