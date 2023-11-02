def solution():
    """If Jason eats three potatoes in 20 minutes, how long, in hours, would it take for him to eat all 27 potatoes cooked by his wife?"""
    num_potatoes = 27
    rate = 3 / 20 # 3 potatoes in 20 minutes
    time_in_hours = num_potatoes / (rate * 60) # convert time to hours
    result = time_in_hours
    return result

print(solution())