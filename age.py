drinking = input('請問你有沒有喝過酒？')
if drinking != '有' and drinking !='沒有':
	print('只能輸入 有/沒有')
	raise SystemExit

age = input('請問你的年齡？')
age = int(age)
if drinking == '有':
	if age >= 18:
		print('你通過測驗了')
	else:
		print('奇怪，未成年怎麼能喝酒！')
elif drinking == '沒有':
	if age >= 18:
		print('我請妳喝酒')
	else:
		print('很好，未成年不能喝酒')

