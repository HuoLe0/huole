import easygui as g

msg = '请填写以下信息'
title = '账号中心'
fieldNames = ['*用户名','*真实姓名','固定电话','*手机号码','QQ','*E-mail']
fieldValues = []
fieldValues = g.multenterbox(msg, title, fieldNames)

while 1:
    if fieldValues == None:
        break
    errmsg = ''
    for i in range(len(fieldValues)):
        option = fieldNames[i].strip() #去除首尾空格
        if fieldValues[i].strip() == '' and option[0] == '*':
            errmsg += ('【%s】为必填。\n\n'%fieldNames[i])
        if errmsg == '':
            break
        fieldValues = g.multenterbox(errmsg,title,fieldNames,fieldValues)

print('用户资料如下：%s'%fieldValues)

