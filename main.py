import os,json
import kivy

#customs
import f_misc as fmisc
import f_str as fstr
import f_math as fmath
import globalshared as gs

from kivy.app import App
from kivy.lang.builder import Builder
from kivy.lang import Builder
from kivy.properties import ObjectProperty,StringProperty,NumericProperty
from kivy.base import runTouchApp
from kivy.core.window import Window


#UIXes
from kivy.uix.popup import Popup
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen , ScreenManager,WipeTransition
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.floatlayout import FloatLayout 

from kivy.clock import Clock

Builder.load_file("kivy.kv")

file = "profile.json"
		

class MousePos(App):
	def build(self):
		from kivy.core.window import Window 
		self.label =Label(pos=(190,190),font_size="10")
		Window.bind(mouse_pos=lambda w,p:setattr(self.label,'text',str(p)))
		return self.label

class statI(App):
	def build(self):
		pass

		return srm

class Win_Name(Screen):
	title_f = gs.font_head()
	norm_f = gs.font_body()
	re_img = gs.reg_img()


	got_name = ObjectProperty()
	name = StringProperty('')

	def get_name(self):
		self.name = self.got_name.text
		print("Assigning name as \"" + self.name + "\"")
		self.save()

	def save(self):
		with open("profile.json","w") as storage:
			json.dump({"BIO":{"name":self.name}},storage,indent=2)

class Win_DOB(Screen):
	title_f = gs.font_head()
	norm_f = gs.font_body()
	re_img = gs.reg_img()

	
	got_year = ObjectProperty()
	year = StringProperty('')

	got_year = ObjectProperty()
	month = StringProperty('')

	got_year = ObjectProperty()
	day = StringProperty('')

	def get_DOB(self):
		months_lis=['','Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sep','Oct','Nov',"Dec"]
		self.year = self.got_year.text
		self.month_str = self.got_month.text
		self.month_num = months_lis.index(self.month_str)
		self.day = self.got_day.text
		print("Assigning year as \"" + self.year + "\"")
		print("Assigning month as \"" + str(self.month_num) + "\"")
		print("Assigning day as \"" + self.day + "\"")
		self.save()

	def save(self):
		with open("profile.json") as intake:
			data = json.load(intake)

		data['BIO']['DOB'] = [self.year,str(self.month_num),self.day]
	
		with open('profile.json',"w") as outgive:
			json.dump(data,outgive,indent=2)	

class Win_Gender(Screen):
	title_f = gs.font_head()
	norm_f = gs.font_body()
	re_img = gs.reg_img()


	got_gender = ObjectProperty()
	gender = StringProperty('')

	def get_gender(self,got_gender):
		self.gender = self.got_gender
		print("Assigning gender as \"" + self.gender + "\"")
		self.save()		
		
	def save(self):
		with open("profile.json") as intake:
			data = json.load(intake)


		data['BIO']['gender'] = self.gender

		with open('profile.json',"w") as outgive:
			json.dump(data,outgive,indent=2)	

class Win_Job(Screen):
	title_f = gs.font_head()
	norm_f = gs.font_body()
	re_img = gs.reg_img()


	got_job = ObjectProperty()
	job = StringProperty('')
	added = StringProperty('')

	def get_job(self):
			self.job = self.got_job.text
			print("Assigning job as \"" + self.job + "\"")
			self.save()

	def save(self):
		with open("profile.json") as intake:
			data = json.load(intake)


		data['BIO']['job'] = self.job

		with open('profile.json',"w") as outgive:
			json.dump(data,outgive,indent=2)	
	

	def build(self):
		pass

class Home_Screen(Screen):
	title_f = gs.font_head()
	norm_f = gs.font_body()
	main_img = gs.main_img()


	fo_siz=18

	nam_e = StringProperty('')
	gender = StringProperty('')
	job = StringProperty('')
	age = StringProperty('')


	def gain_info(self):
		with open("profile.json") as intake:
			data = json.load(intake)

		in_nam_e = data['BIO']['name']
		in_dob = data['BIO']['DOB']
		in_gen_der = data['BIO']['gender']
		in_job = data['BIO']['job']
		in_name_lis = fstr.fucc_str_to_words(in_nam_e)
		in_age_lis = fmisc.get_age(in_dob)
		in_age = fstr.fucc_list_2_string(in_age_lis,":")
		if in_gen_der == "male":
			in_gender="M"
		elif in_gen_der == "female":
			in_gender="F"
		else:
			in_gender="O"

		self.nam_e = in_nam_e
		self.dob = in_dob
		self.age = in_age
		self.gender = in_gender
		self.job = in_job
		print("done")

class Details(Screen):
	title_f = gs.font_head()
	norm_f = gs.font_body()
	re_img = gs.reg_img()

	y = NumericProperty(0)
	jj = StringProperty('')
	text = StringProperty("Ok Then")
	blabla = ''

	def get_data(self):
		with open('profile.json') as file:
			data = json.load(file)

		nae = data['BIO']['name']
		dob = data['BIO']['DOB']
		gender = data['BIO']['gender']
		name_lis = fstr.fucc_str_to_words(nae)
		
		da = ("Hello user," + " \nFrom the information I acquired \n from you, \n I Got that, \nYour name is : " + nae + " ,"+  "\nYour DateOfBirth is: "  + str(dob[0])+"/"+str(dob[1])+"/"+str(dob[2])+"\nand"+"\nYou are a " + gender+" ,"+"\nNow we would like you to enter \n your current job")
		self.blabla = da
		self.clicked()
		

	def build(self):
		pass

	def clicked(self, i=0):
	 def clicked2(self):
	 	nonlocal i; i += 1
	 	if i > len(self.blabla): return False
	 	self.text = self.blabla[:i]
	 	self.jj = 'Job Screen>>'

	 Clock.schedule_interval(lambda count: clicked2(self), .05)

srm = ScreenManager(transition=WipeTransition())

if not(os.path.exists(file)):
	srm.add_widget(Win_Name(name="name_s"))
	srm.current = "name_s"
	srm.add_widget(Win_DOB(name="dob_s"))
	srm.add_widget(Win_Gender(name="gender_s"))
	srm.add_widget(Details(name="det"))
	srm.add_widget(Win_Job(name="job_s"))
	srm.add_widget(Home_Screen(name="home_s"))

if os.path.exists(file):
	srm.add_widget(Home_Screen(name="home_s"))
	print("Yes")
	srm.current = 'home_s'
	

if __name__ == '__main__':
		statI().run()
