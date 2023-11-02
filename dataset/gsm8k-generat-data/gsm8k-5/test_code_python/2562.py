def solution():
    potatoes_per_20_min = 3  # Jason eats 3 potatoes in 20 minutes
    total_potatoes = 27  # Jason wants to eat all 27 potatoes cooked by his wife

    # Calculate the total number of 20-minute intervals needed to eat all the potatoes
    intervals = total_potatoes // potatoes_per_20_min
    if total_potatoes % potatoes_per_20_min != 0:
        intervals += 1

    # Convert the total number of 20-minute intervals to hours
    hours = intervals / 3  # There are 3 20-minute intervals in an hour
    result = hours
    return result

print(solution())