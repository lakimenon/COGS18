""" Module containing tests for certain functions"""
import random
from game_module import functions
from game_module import classes

def test_reset_location():
	""" Function to test reset_location function"""
	test_rock =  classes.Rock('./icons/rock.png', 100, -600, 48, 69, 4)

	functions.reset_location(test_rock)
	assert test_rock.height == 48
	assert test_rock.y == -48
	assert 0 < test_rock.x < 800 - test_rock.width	#800 = display width

def test_overlap():
	""" Function to test overlap function"""
	test_rock =  classes.Rock('./icons/rock.png', 100, -600, 48, 69, 4)
	player_x = 800*0.45
	player_y = 600-94
	test_player = classes.Player('./icons/basket.png', player_x, player_y, 94, 139, 0)

	#Same y, different x => Does not overlap
	test_rock.y = test_player.y
	assert not functions.overlap(test_player, test_rock)

	#Same x, different y => Does not overlap
	test_rock.x = test_player.x
	test_rock.y = 0
	assert not functions.overlap(test_player, test_rock)

	#Rock's left side overlaps with player
	test_rock.x = random.randrange(test_player.x, test_player.x + test_player.width)
	test_rock.y = random.randrange(test_player.y - test_rock.height, 600)
	assert functions.overlap(test_player, test_rock)

	#Rock overlaps entirely within player
	test_rock.x = random.randrange(test_player.x, test_player.x + test_player.width - test_rock.width)
	test_rock.y = random.randrange(test_player.y - test_rock.height, 600)
	assert functions.overlap(test_player, test_rock)

	#Rock's right side overlaps with player
	test_rock.x = random.randrange(test_player.x - test_rock.width, test_player.x + test_player.width - test_rock.width)
	test_rock.y = random.randrange(test_player.y - test_rock.height, 600)
	assert functions.overlap(test_player, test_rock)
