def solution():
     total_marbles = 50
     initial_white_marbles = 20
     initial_red_marbles = (total_marbles - initial_white_marbles) / 2
     initial_blue_marbles = initial_red_marbles
     white_marble_difference = initial_white_marbles - initial_blue_marbles
     double_difference = white_marble_difference * 2
     jack_removed = double_difference
     marbles_left = total_marbles - jack_removed
     result = marbles_left
 
     return result

print(solution())