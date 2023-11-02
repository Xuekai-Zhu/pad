def solution():
    
    tomatoes_planted = 3 * 5
    cucumbers_planted = 5 * 4
    potatoes_planted = 30
    total_planted = tomatoes_planted + cucumbers_planted + potatoes_planted
    total_spaces = 10 * 15
    remaining_spaces = total_spaces - total_planted
    result = remaining_spaces
    return result

print(solution())