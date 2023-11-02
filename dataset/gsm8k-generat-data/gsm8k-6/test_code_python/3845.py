def solution():
    # Calculate the number of mushrooms picked on the second and third day
    mushrooms_day2 = 12
    mushrooms_day3 = 2 * mushrooms_day2
    
    # Calculate the total number of mushrooms picked
    total_mushrooms = mushrooms_day2 + mushrooms_day3
    
    # Calculate the total amount earned from selling all the mushrooms
    total_money = 58 + (total_mushrooms * 2)  # $2 per mushroom
    
    result = total_mushrooms
    return result

print(solution())