import pygame
from settings import Settings
from ship import Ship
import game_function as gf
from pygame.sprite import Group
from alien import Alien
from scoreboard import Scoreboard
from game_stats import GameStats
from button import Button


def run_game():
	#initilize the game and create a screen object
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption('Alien Invasion')
	play_button = Button(ai_settings,screen,"Play")
	ship = Ship(ai_settings,screen)
	bullets = Group()
	alien = Alien(ai_settings,screen)
	aliens = Group()
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings,screen,stats)


	#set background color
	

	#begin the major loop

	while True:
		#keyboard and mouse event 
		gf.check_event(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
		
		
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
			gf.update_aliens(ai_settings,stats,screen,sb,ship,aliens,bullets)
		gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)
		#reset background color
		#display the current screen
	
		
run_game()

    
