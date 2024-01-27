
try:
	import pygame
	import sys
	import time
	import math

	pygame.init() #Khoi tao pygame

	screen= pygame.display.set_mode((500,600)) #vong lap

	GREY= (150,150,150) #constant variable: bien khong doi nen phai viet hoa
	WHITE=(255,255,255)
	RED=(255,25,64)
	BLACK=(0,0,0)
	running=True

	font=pygame.font.SysFont('sans',50)
	text_1=font.render('+',True,BLACK) #true giup lam chu muot hon
	text_2=font.render('+',True,BLACK)
	text_3=font.render('-',True,BLACK)
	text_4= font.render('-',True,BLACK)
	text_5=font.render('START',True,BLACK)
	text_6=font.render('RESET',True,BLACK)

	total_secs=0
	total=0
	start=False

	sound= pygame.mixer.Sound('clockrun_1.wav')
	sound_2=pygame.mixer.Sound('clockend.wav')
	clock=pygame.time.Clock()

	while running:
		clock.tick(60)
		screen.fill(GREY)
		
		mouse_x, mouse_y= pygame.mouse.get_pos() #gte_pos lay vi tri con chuot
		
		pygame.draw.rect(screen,WHITE,(50,50,50,50))
		pygame.draw.rect(screen,WHITE,(150,50,50,50))
		pygame.draw.rect(screen,WHITE,(50,150,50,50))
		pygame.draw.rect(screen,WHITE,(150,150,50,50))
		pygame.draw.rect(screen,WHITE,(300,150,150,50))
		pygame.draw.rect(screen,WHITE,(300,150,150,50))
		pygame.draw.rect(screen,WHITE,(300,50,150,50))


		screen.blit(text_1,(60,50))
		screen.blit(text_2,(160,50))
		screen.blit(text_3,(70,140))
		screen.blit(text_4,(170,140))
		screen.blit(text_5,(300,50))
		screen.blit(text_6,(300,150))

		
		pygame.draw.rect(screen,BLACK,(50,520,400,50))
		pygame.draw.rect(screen,WHITE,(60,530,380,30))
		

		pygame.draw.circle(screen,BLACK,(250,400),100) # lan luot kich co hinh tron theo toa do (x,y),r
		pygame.draw.circle(screen, WHITE,(250,400),95)
		pygame.draw.circle(screen, BLACK, (250,400),5)
		
		#pygame.draw.line(screen, BLACK,(250,400),(250,310)) #toa do (x,y),(phuong huong, do dai)


		for event in pygame.event.get(): #xet cac su kien phim, nut tat
			if event.type==pygame.QUIT: #type loai event
				running=False
			if event.type== pygame.MOUSEBUTTONDOWN:
				if event.button==1:
					pygame.mixer.pause()
				if mouse_x<100 and mouse_x>50:
					if mouse_y>50 and mouse_y<100:
						total_secs+=60
						print("press plus minute")
				if mouse_x<100 and mouse_x>50:
					if mouse_y>150 and mouse_y<200:
						total_secs-=60
						print("press - minute")
				if mouse_x>150 and mouse_x<200:
					if mouse_y<100 and mouse_y>50:
						total_secs+=1
						print("press plus second")
				if mouse_x>150 and mouse_x<200:
					if mouse_y>150 and mouse_y<200:
						total_secs-=1
						print("press - second")
				if mouse_x>300 and mouse_x<450:
					if mouse_y<150 and mouse_y>50:
						start =True
						total=total_secs
						print("press START")
				if mouse_x>300 and mouse_x<450:
					if mouse_y<200 and mouse_y>150:
						total_secs=0
						print("press Reset")
					print("total_secs:"+str(total_secs))

		if start:
			total_secs-=1
			pygame.mixer.Sound.play(sound)
			if total_secs==0:
				start=False
				pygame.mixer.Sound.stop(sound)
				pygame.mixer.Sound.play(sound_2)
			time.sleep(1)
		if total_secs<0:
			total_secs=0


		mins=int(total_secs/60)
		secs=total_secs - mins*60

		time_now=str(mins)+ ":" +str(secs)

		
		text_time=font.render(time_now,True,BLACK)
		screen.blit(text_time, (100,100))
		
		x_sec=250 + 90* math.sin(6* secs* math.pi/180)
		y_sec=400 - 90* math.cos(6* secs* math.pi/180)
		pygame.draw.line(screen, RED, (250,400),(int(x_sec),int(y_sec)))

		x_min=250 + 40* math.sin(6* mins* math.pi/180)
		y_min=400 - 40* math.cos(6* mins* math.pi/180)
		pygame.draw.line(screen, BLACK, (250,400), (int(x_min),int(y_min)))

		if total!=0:
			pygame.draw.rect(screen, RED,(60,530,int(380*(total_secs/total)),30))
				

		pygame.display.flip() #Hien mau da code tren cua so

	pygame.quit()

except Exception as bug:
	print(bug)


