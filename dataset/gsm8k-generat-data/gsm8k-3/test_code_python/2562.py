def solution():
    """If Jason eats three potatoes in 20 minutes, how long, in hours, would it take for him to eat all 27 potatoes cooked by his wife?"""
    # Define the rate at which Jason eats potatoes
    RATE = 3 / (20/60) # 3 potatoes in 20 minutes, converted to potatoes per hour

    # Calculate the time it takes to eat all 27 potatoes
    time = 27 / RATE # potatoes / (potatoes / hour) = hours

    # Display the time it takes to eat all the potatoes
    result = time
    return result

print(solution())