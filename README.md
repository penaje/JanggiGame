An implementation of "Janggi", a sort of chess like game.

I did not implement the rules regarding perpetual check, position repetition, any kind of draw.

Here's a very simple example of how the game could be played:
```
game = JanggiGame()
move_result = game.make_move('c1', 'e3') #should be False because it's not Red's turn
move_result = game.make_move('a7,'b7') #should return True
blue_in_check = game.is_in_check('blue') #should return False
game.make_move('a4', 'a5') #should return True
state = game.get_game_state() #should return UNFINISHED
game.make_move('b7','b6') #should return True
game.make_move('b3','b6') #should return False because it's an invalid move
game.make_move('a1','a4') #should return True
game.make_move('c7','d7') #should return True
game.make_move('a4','a4') #this will pass the Red's turn and return True
```

