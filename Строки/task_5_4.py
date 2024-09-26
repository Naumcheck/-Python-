'''

Напишите программу, основываясь на вводе и выводе в примерах. Вводом будет строка a. Результат сохраните в result.  

a = "div*2"
result = "<div></div><div></div>"

a = "p*1" 
result = "<p></p>"

a = "li*3"
result = "<li></li><li></li><li></li>"


'''
tmp = a.split('*')[0]
result = ('<' + tmp + '>' + '<' + '/' + tmp + '>') * int(a.split('*')[1])