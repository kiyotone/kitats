import f_misc as fmisc 
import f_math as fmath



def fucc_extract_lett(string):
	chars=[]
	for x in range(len(string)):
		if string[x] != " ":
			chars.append(string[x])

	return chars

def fucc_str_to_words(string):
	wrd_no=0
	chr_no =len(string)
	x_string=string+" "
	wrd =[]
	sp=0

	for cou in range(chr_no+1):
		if x_string[cou] == " ":
			wrd_no+=1
			word=""
			for x in range(sp,cou):
				word+=x_string[x]
			wrd.append(word)
			sp=cou+1

	return wrd

def fucc_is_char(char):
	characters={"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",} 
	if char in characters:
		return True
	else:
		return False

def fucc_list_2_string(lis,div):
	string=""
	stri=""
	for x in range(len(lis)):
		string= string+str(lis[x])+str(div)

	for y in range(len(string)-1):
		stri = stri + string[y]
	
	return stri
