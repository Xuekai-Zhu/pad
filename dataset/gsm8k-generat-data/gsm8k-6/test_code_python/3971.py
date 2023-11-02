def solution():
    # Calculate the total distance Mona biked this week
    total_distance = 30 * 3 # Mona bikes 30 miles each week and biked on Monday, Wednesday, and Saturday
    
    # Calculate the distance Mona biked on Saturday
    distance_on_Saturday = total_distance - 12 - 30 # Mona biked on Monday and Wednesday already, and biked twice as far as on Monday on Saturday
    
    # Calculate the distance Mona biked on Monday
    distance_on_Monday = (total_distance - 12 - distance_on_Saturday) / 2 # Mona biked on Wednesday already, and the distance on Monday is half of the remaining distance
    
    result = distance_on_Monday
    return result

print(solution())