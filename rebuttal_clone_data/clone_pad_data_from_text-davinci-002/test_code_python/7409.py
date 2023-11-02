def solution():
    rolls_of_toilet_paper = 1000
    squares_of_toilet_paper = 300
    squares_used_per_day = 3 * 5
    squares_used_per_week = squares_used_per_day * 7
    squares_used_per_roll = squares_of_toilet_paper / squares_used_per_week
    result = rolls_of_toilet_paper / squares_used_per_roll
    
    return result

print(solution())