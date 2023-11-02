def solution():
    total_pebbles = 40
    red_pebbles = 9
    blue_pebbles = 13
    
    # Calculate the number of remaining pebbles
    remaining_pebbles = total_pebbles - red_pebbles - blue_pebbles
    
    # Divide the remaining pebbles into 3 groups
    divided_pebbles = remaining_pebbles // 3
    
    # Paint the divided pebbles purple, yellow, and green
    purple_pebbles = divided_pebbles
    yellow_pebbles = divided_pebbles
    green_pebbles = divided_pebbles
    
    # Calculate the difference between the number of blue and yellow pebbles
    difference = blue_pebbles - yellow_pebbles
    result = difference
    return result

print(solution())