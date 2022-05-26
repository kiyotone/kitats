
import f_misc as fmisc 
import f_str as fstr
	

def fucc_sum(string):
	num = extract_num(string)
	a=0
	sum_fin=int(a)
	for i in range(len(num)):
		sum_fin += int(num[i])
	
	final = str(sum_fin)
	return final

def fucc_prod(string):
	num = extract_num(string)
	prod_fin=1
	for i in range(len(num)):
		prod_fin *= int(num[i])
	
	final = str(prod_fin)
	return final

def fucc_diff(string):
	num = extract_num(string)
	strs = fstr.str_to_words(string)
	last = len(num)-1
		
	diff = int(num[last])
	num.pop(last)

	for x in range(0,len(num)):
		diff -= int(num[x])

	return diff

def fucc_dmas(data):
	ans = 0
	f_ans=0

	eqn = fucc_eqn_creater(data)

	if eqn[0].isdigit():
		eqn.insert(0,"+")

	nums = []
	for x in range(len(eqn)):
		if eqn[x].isdigit():
			nums.append(eqn[x])

	div_no=0
	mul_no=0
	add_no=0
	sub_no=0

	su =[]
	temp = ""
	run=True

	d_done = True
	m_done = True
	as_done= True
	while run ==True:
		
		if d_done ==True and m_done ==True and as_done ==True:
			run = False


		for x in range(len(eqn)):
			if eqn[x]=="/":
				div_no+=1
			if eqn[x]=="*":
				mul_no+=1
			if eqn[x]=="+":
				add_no+=1

			if eqn[x]=="-":
				sub_no+=1

		for x in range(div_no):
			
			if "/" in eqn:
				xf = eqn.index("/")
				f1 = float(nums[int((xf-1)/2)]) 
				f2 = float(nums[int((xf+1)/2)]) 	
				ans = f1 / f2
				del nums[int((xf-1)/2) : int(((xf+1)/2)+1)]	
				del eqn[xf-1:xf+2]
				eqn.insert(xf-1,ans)
				nums.insert(int((xf-1)/2),ans)
			
		if "/" in eqn:
			d_done = True

		for x in range(mul_no):
			
			if "*" in eqn:
				xf = eqn.index("*")
				f1 = float(nums[int((xf-1)/2)]) 
				f2 = float(nums[int((xf+1)/2)]) 	
				ans = f1 * f2
				del nums[int((xf-1)/2) : int(((xf+1)/2)+1)]	
				del eqn[xf-1:xf+2]
				eqn.insert(xf-1,ans)
				nums.insert(int((xf-1)/2),ans)
			
		if "*" in eqn:
			m_done = True

		for x in range(len(eqn)):
				if eqn[x]=="+":	
					su.append(eqn[x+1])
					
				elif eqn[x] == "-":
					su.append(int(eqn[x+1])*(-1))
		
		eqn.clear()

		for x in range(len(su)):
			f_ans = f_ans+int(su[x])

		if len(eqn) == 0:
			as_done =True
	return f_ans

def fucc_calculate(string):
	
	symbols = {"*" , "/" , "+" , "-" , "(" , ")" , "{" , "[" , "]" , "}"}

	strs=fstr_fucc_extract_lett(string)
	syms= []
	num=fucc_extract_num(string)
	eqn= []
	vals= []

	for x in range(len(strs)):
		if not(fstr.fucc_is_char(strs[x])) and strs[x]!=" ":
			eqn.append(strs[x])

	return eqn

def fucc_eqn_creater(string):
	symbols = {"*" , "/" , "+" , "-" , "(" , ")" , "{" , "[" , "]" , "}"}
	final=[]
	com_no=[]
	ltts=fstr.fucc_extract_lett(string)
	for x in range(len(ltts)):
		if not((fstr.fucc_is_char(ltts[x]))):
			com_no.append(ltts[x])


	dio = fstr.fucc_list_2_string(com_no)		
	dio=dio + "/"
	y=0
	wrd=""

	for x in range(len(dio)):
		if not(dio[x].isdigit()):
			for q in range(y,x):
			 	wrd = wrd+dio[q]
			y=x+1
			final.append(wrd)
			wrd=""
		if dio[x] in symbols:
			final.append(dio[x])

	final.pop()

	return final

def fucc_extract_num(string):
	num=[]
	
	wrd=fstr.fucc_str_to_words(string)
	wrd_no=len(wrd)
	
	for x in range(wrd_no):
		if wrd[x].isdigit():
			num.append(wrd[x])

	return num
