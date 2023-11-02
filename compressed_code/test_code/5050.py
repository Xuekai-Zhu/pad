def solution():
    
    second_game = 80
    first_game = second_game - 20
    third_game = second_game + 15
    total_this_week = first_game + second_game + third_game
    total_last_week = 200
    difference = total_this_week - total_last_week
    result = difference
    return result

print(solution())