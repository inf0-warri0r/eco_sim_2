"""
Author : tharindra galahena (inf0_warri0r)
Project: artificial life simulation #2
Blog   : http://www.inf0warri0r.blogspot.com
Date   : 29/08/2013
License:

	 Copyright 2014 Tharindra Galahena

This is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version. This is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
details.

* You should have received a copy of the GNU General Public License along with
this. If not, see http://www.gnu.org/licenses/.

"""


import random
from Tkinter import *


class type_one:
	def __init__(self, mut):
		self.env = list()
		self.env_tmp = list()
		self.env_color = list()
		self.env_color_tmp = list()
		self.mutation = mut
		
		for i in range(0, 50):
			tmp = list()
			tmp2 = list()
			tmp_c = list()
			tmp_c_2 = list()
			for j in range(0, 50):
				tmp.append(0)
				tmp2.append(0)
				tmp_c.append((0, 0, 0))
				tmp_c_2.append((0, 0, 0))
			self.env.append(tmp)
			self.env_tmp.append(tmp2)
			self.env_color.append(tmp_c)
			self.env_color_tmp.append(tmp_c_2)

	def reproduct(self, p, q, type_two_env):

		lst = list()
		for y in range(q - 1, q + 2):
			for x in range(p - 1, p + 2):
				if x >= 0 and y >= 0 and x < 50 and y < 50:
					if self.env[y][x] == 0 and type_two_env[y][x] == 0:
						lst.append((x, y))

		if len(lst) > 0:
			n = random.randint(0, len(lst) - 1)
			mutation_r = random.randint(0, self.mutation) - self.mutation / 2.0
			mutation_b = random.randint(0, self.mutation) - self.mutation / 2.0
			mutation_g = random.randint(0, self.mutation) - self.mutation / 2.0
						
			if self.env_color[q][p][0] >= 255 - self.mutation / 2.0:
				mutation_r = -self.mutation / 2.0
			elif self.env_color[q][p][0] <= self.mutation / 2.0:
				mutation_r = self.mutation / 2.0
				
			if self.env_color[q][p][1] >= 255 - self.mutation / 2.0:
				mutation_g = -self.mutation / 2.0
			elif self.env_color[q][p][1] <= self.mutation / 2.0:
				mutation_g = self.mutation / 2.0
				
			if self.env_color[q][p][2] >= 255 - self.mutation / 2.0:
				mutation_b = -self.mutation / 2.0
			elif self.env_color[q][p][2] <= self.mutation / 2.0:
				mutation_b = self.mutation / 2.0
				
			self.env_tmp[lst[n][1]][lst[n][0]] = 1
			self.env_color_tmp[lst[n][1]][lst[n][0]] = self.env_color[q][p][0] + mutation_r, self.env_color[q][p][1] + mutation_g, self.env_color[q][p][2] + mutation_b
			
	def grow(self, x, y):
		if self.env[y][x] > 0 and self.env[y][x] < 12:
			self.env_tmp[y][x] = self.env[y][x] + 1
			self.env_color_tmp[y][x] = self.env_color[y][x]
		elif self.env[y][x] == 12:
			self.env_tmp[y][x] = self.env[y][x]
			self.env_color_tmp[y][x] = self.env_color[y][x]
		

	def swap(self):
		for y in range(0, 50):
			for x in range(0, 50):
				self.env[y][x] = self.env_tmp[y][x]
				self.env_color[y][x] = self.env_color_tmp[y][x]
				self.env_tmp[y][x] = 0

	def next_gen(self, type_two_env):
		for y in range(0, 50):
			for x in range(0, 50):
				self.grow(x, y)

		for y in range(0, 50):
			for x in range(0, 50):
				if self.env[y][x] > 0:
					self.reproduct(x, y, type_two_env)
					
		self.swap()

	def reset(self):
		for y in range(0, 50):
			for x in range(0, 50):
				self.env[y][x] = 0
				self.env_tmp[y][x] = 0
				self.env_color[y][x] = 0
				self.env_color_tmp[y][x] = 0


class type_two:

	def __init__(self, mut):
		self.env = list()
		self.env_tmp = list()
		self.env_color = list()
		self.env_color_tmp = list()
		self.mutation = mut
		
		for i in range(0, 50):
			tmp = list()
			tmp2 = list()
			tmp_c = list()
			tmp_c_2 = list()
			for j in range(0, 50):
				tmp.append(0)
				tmp2.append(0)
				tmp_c.append((0, 0, 0))
				tmp_c_2.append((0, 0, 0))
			self.env.append(tmp)
			self.env_tmp.append(tmp2)
			self.env_color.append(tmp_c)
			self.env_color_tmp.append(tmp_c_2)
			
	def reproduct(self, p, q, type_one_env, type_one_color):

		lst = list()
		mutation_r = random.randint(0, self.mutation) - self.mutation / 2.0
		mutation_b = random.randint(0, self.mutation) - self.mutation / 2.0
		mutation_g = random.randint(0, self.mutation) - self.mutation / 2.0
					
		if self.env_color[q][p][0] >= 255 - self.mutation / 2.0:
			mutation_r = -self.mutation / 2.0
		elif self.env_color[q][p][0] <= self.mutation / 2.0:
			mutation_r = self.mutation / 2.0
			
		if self.env_color[q][p][1] >= 255 - self.mutation / 2.0:
			mutation_g = -self.mutation / 2.0
		elif self.env_color[q][p][1] <= self.mutation / 2.0:
			mutation_g = self.mutation / 2.0
			
		if self.env_color[q][p][2] >= 255 - self.mutation / 2.0:
			mutation_b = -self.mutation / 2.0
		elif self.env_color[q][p][2] <= self.mutation / 2.0:
			mutation_b = self.mutation / 2.0
				
		color = self.env_color[q][p][0] + mutation_r, self.env_color[q][p][1] + mutation_g, self.env_color[q][p][2] + mutation_b
		
		for y in range(q - 1, q + 2):
			for x in range(p - 1, p + 2):
				if x >= 0 and y >= 0 and x < 50 and y < 50:
					if self.env[y][x] == 0:
						mutation_r = random.randint(0, 10) - 5
						mutation_b = random.randint(0, 10) - 5
						mutation_g = random.randint(0, 10) - 5
						
						if self.env_color[q][p][0] >= 255:
							mutation_r = -5
						elif self.env_color[q][p][0] <= 5:
							mutation_r = 5
							
						if self.env_color[q][p][1] >= 255:
							mutation_g = -5
						elif self.env_color[q][p][1] <= 5:
							mutation_g = 5
							
						if self.env_color[q][p][2] >= 255:
							mutation_b = -5
						elif self.env_color[q][p][2] <= 5:
							mutation_b = 5
								
						color = self.env_color[q][p][0] + mutation_r, self.env_color[q][p][1] + mutation_g, self.env_color[q][p][2] + mutation_b
						if type_one_env[y][x] > 0:
							if type_one_color[y][x][0] - color[0] > -30 and type_one_color[y][x][0] - color[0] < 30:
								lst.append((x, y, color))
							elif type_one_color[y][x][1] - color[1] > -30 and type_one_color[y][x][1] - color[1] < 30:
								lst.append((x, y, color))
							elif type_one_color[y][x][2] - color[2] > -30 and type_one_color[y][x][2] - color[2] < 30:
								lst.append((x, y, color))
						elif type_one_env[y][x] == 0:
							lst.append((x, y, color))

		if len(lst) > 0:
			n = random.randint(0, len(lst) - 1)
						
			self.env_tmp[lst[n][1]][lst[n][0]] = 1
			self.env_color_tmp[lst[n][1]][lst[n][0]] = lst[n][2]
			type_one_env[lst[n][1]][lst[n][0]] = 0
				
				
			self.env_tmp[q][p] = self.env[q][p]
			self.env_color_tmp[q][p] = self.env_color[q][p]
		
	def feed(self, p, q, type_one_env, type_one_color):
		lst = list()
		for y in range(q - 1, q + 2):
			for x in range(p - 1, p + 2):
				if x >= 0 and y >= 0 and x < 50 and y < 50:
					if type_one_env[y][x] > 0 :
						if type_one_color[y][x][0] - self.env_color[q][p][0] > -30 and type_one_color[y][x][0] - self.env_color[q][p][0] < 30:
							if type_one_color[y][x][1] - self.env_color[q][p][1] > -30 and type_one_color[y][x][1] - self.env_color[q][p][1] < 30:
								if type_one_color[y][x][2] - self.env_color[q][p][2] > -30 and type_one_color[y][x][2] - self.env_color[q][p][2] < 30:
									lst.append((x, y))

		if len(lst) > 0:
			n = random.randint(0, len(lst) - 1)
			self.env_tmp[lst[n][1]][lst[n][0]] = self.env[q][p]
			self.env_color_tmp[lst[n][1]][lst[n][0]] = self.env_color[q][p]
			self.env_tmp[lst[n][1]][lst[n][0]] = self.env[q][p] + 1
			self.env[q][p] = 0
			self.env_color[q][p] = 0
			type_one_env[lst[n][1]][lst[n][0]] = 0
			type_one_color[lst[n][1]][lst[n][0]] = 0
		else:
			if self.env[q][p] > 0:
				self.env_tmp[q][p] = self.env[q][p] - 1
				self.env_color_tmp[q][p] = self.env_color[q][p]

	def swap(self):
		for y in range(0, 50):
			for x in range(0, 50):
				self.env[y][x] = self.env_tmp[y][x]
				self.env_color[y][x] = self.env_color_tmp[y][x]
				self.env_tmp[y][x] = 0

	def next_gen(self, type_one_env, type_one_color):
		for y in range(0, 50):
			for x in range(0, 50):
				if self.env[y][x] > 0:
					self.feed(x, y, type_one_env, type_one_color)

		self.swap()

		for y in range(0, 50):
			for x in range(0, 50):
				if self.env[y][x] > 0:
					self.reproduct(x, y, type_one_env, type_one_color)

		self.swap()

	def reset(self):
		for y in range(0, 50):
			for x in range(0, 50):
				self.env[y][x] = 0
				self.env_tmp[y][x] = 0
				self.env_color[y][x] = 0
				self.env_color_tmp[y][x] = 0

################################### display ##################################

root = Tk()
root.title("Artificial Life Simulation #2")

cw = 600
ch = 700

chart_1 = Canvas(root, width=cw, height=ch, background="black")
chart_1.grid(row=0, column=0)


ec = type_one(10)
an = type_two(20)

started = False
step_time = 50
reset = False
pause = False

def rgb_to_hex(rgb):
	r, g, b = rgb
	if r < 0:
		r = 0
	if r > 255:
		r = 255
	
	if g < 0:
		g = 0
	if g > 255:
		g = 255
	
	if b < 0:
		b = 0
	if b > 255:
		b = 255
	
	rgb = r, g, b
	
	return '#%02x%02x%02x' % rgb

def callback(event):
	global started
	x = int(event.x / 12)
	y = int(event.y / 12)
	if x < 50 and y < 50:
		started = True
		ec.env[y][x] = 1
		ec.env_color[y][x] = 128, 0, 0


def callback2(event):
	x = int(event.x / 12)
	y = int(event.y / 12)
	if x < 50 and y < 50:
		an.env[y][x] = 1
		an.env_color[y][x] = ec.env_color[y][x]


def speed(event):
	global step_time
	if event.keysym == "Up":
		if step_time > 0:
			step_time = step_time - 1
	elif event.keysym == "Down":
		step_time = step_time + 1


def reset_func(event):
	global reset
	reset = True


def pause_func(event):
	global pause
	if pause:
		pause = False
	else:
		pause = True

chart_1.bind("<Button-1>", callback)
chart_1.bind("<Button-3>", callback2)
chart_1.bind_all("<KeyPress-Up>", speed)
chart_1.bind_all("<KeyPress-Down>", speed)
chart_1.bind_all("<KeyPress-r>", reset_func)
chart_1.bind_all("<KeyPress-p>", pause_func)

steps = 0

while 1:

	if(started) and not pause:
		steps = steps + 1

	for y in range(0, 50):
		for x in range(0, 50):
			if ec.env[y][x] > 0:
				chart_1.create_oval((x * 12 + 6) - 6,
									(y * 12 + 6) - 6,
									(x * 12 + 6) + 6,
									(y * 12 + 6) + 6, 
									fill=rgb_to_hex(ec.env_color[y][x]))
			if an.env[y][x] > 0:

				chart_1.create_oval((x * 12 + 6) - 4,
									(y * 12 + 6) - 4,
									(x * 12 + 6) + 4,
									(y * 12 + 6) + 4,
									fill='blue')

	chart_1.create_line(0, 600, 600, 600, fill="white")

	chart_1.create_text(100, 650,
		text="steps = " + str(steps) + " step time = " + str(step_time),
		fill='white')

	if not pause:
		ec.next_gen(an.env)
		an.next_gen(ec.env, ec.env_color)

	if reset:
		ec.reset()
		an.reset()
		reset = False
		started = False
		steps = 0
		
	chart_1.update()
	chart_1.after(step_time)
	
	chart_1.delete(ALL)
	
root.mainloop()

