import pygame, random

pygame.init()

screen = pygame.display.set_mode((500, 600))
pygame.display.set_caption("Rắn săn mồi được tạo bởi MINH NHẬT")

#color
GREY = (150,150,150) #xám
WHITE = (250,250,250) #trắng
RED = (250,0,0) #đỏ
BLACK = (0,0,0) #đen
YELLOW = (255,255,102) #vàng
BLUE = (173,216,230) 
#time
clock = pygame.time.Clock()
snake_speed = 30

font_style = pygame.font.SysFont(None, 20)
score_font = pygame.font.SysFont(None, 30)


def YourScore(score):
	value = score_font.render("Score: " + str(score), True, YELLOW)
	screen.blit(value, [0,0])


def HighScore(file_path):
	file = open(file_path, mode = 'r')
	list = []
	for ch in file:
		list.append(int(ch))
	file.close()
	list.sort(reverse = True)
	highscore = score_font.render("High Score: " + str(list[0]), True, YELLOW)
	screen.blit(highscore, [100,0])
def message(msg, color, score, file_path):
	mes = font_style.render(msg, True, color)
	screen.blit(mes, [100, 200])
	YourScore(score)
	HighScore(file_path)
def our_snake(snake_block, snake_list):
	for snake in snake_list:
		pygame.draw.rect(screen, WHITE, [snake[0], snake[1], snake_block, snake_block])

def check_collision(food_x, food_y, x_pos, y_pos):
	if x_pos + 10 >= food_x and x_pos + 10 <= food_x + 20:
		if y_pos + 10 >= food_y and y_pos + 10 <= food_y + 20:
			return True
	if x_pos >= food_x and x_pos <= food_x + 20:
		if y_pos + 10 >= food_y and y_pos + 10 <= food_y + 20:
			return True
	if x_pos + 10 >= food_x and x_pos + 10 <= food_x + 20:
		if y_pos >= food_y and y_pos <= food_y + 20:
			return True
	if x_pos >= food_x and x_pos <= food_x + 20:
		if y_pos >= food_y and y_pos <= food_y + 20:
			return True
def game_loop():
	running = True
	game_over = False
	#setting
	x_pos = 300
	y_pos = 300
	x_val = 5
	y_val = 0

	snake_list = []
	size_of_snake = 1

	food_x = round(random.randrange(40, 400 - 10) / 10) * 10
	food_y = round(random.randrange(40, 500 - 10) / 10) * 10
	
	while running:
		score_final = size_of_snake - 1
		file = open('high_score.txt', mode = 'a')
		file.write(str(score_final) + '\n')
		file.close()
		while game_over:
			screen.fill(GREY)
			message("You lost! Press C to play again or Q to Quit", RED, size_of_snake - 1, 'high_score.txt')
			pygame.display.update()

			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						running = False
						game_over = False
					if event.key == pygame.K_c:
						game_loop()
				
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_val = -5
					y_val = 0
				elif event.key == pygame.K_RIGHT:
					x_val = 5
					y_val = 0
				elif event.key == pygame.K_UP:
					x_val = 0
					y_val = -5
				elif event.key == pygame.K_DOWN:
					x_val = 0
					y_val = 5

		if x_pos < 40 or x_pos >= 440 or y_pos < 40 or y_pos >= 540:
			game_over = True
			
		x_pos += x_val
		y_pos += y_val

		screen.fill(GREY)
		pygame.draw.rect(screen, BLACK, (30,30,440,540))
		pygame.draw.rect(screen, BLUE, (40,40,420,520))
		pygame.draw.rect(screen, RED, (food_x,food_y,20,20))

		snake_head = []
		snake_head.append(x_pos)
		snake_head.append(y_pos)
		snake_list.append(snake_head)

		if len(snake_list) > size_of_snake:
			del snake_list[0]

		for snake in snake_list[:-1]:
			if snake == snake_head:
				game_over = True

		our_snake(10, snake_list)
		YourScore(size_of_snake-1)
		HighScore('high_score.txt')
		pygame.display.update()
		
		#check collision
		if check_collision(food_x, food_y, x_pos, y_pos) == True:
			food_x = round(random.randrange(40, 400 - 10) / 10.0) * 10.0
			food_y = round(random.randrange(40, 500 - 10) / 10.0) * 10.0
			size_of_snake += 5

		clock.tick(snake_speed)
	
	pygame.quit()
	quit()
	

game_loop()