def solution():
    # Calculate the number of spotted and gilled mushrooms on the fallen log
    total_mushrooms = 30
    spotted_mushrooms = total_mushrooms / 10  # gilled mushrooms grow 1 for every 9 spotted mushrooms
    gilled_mushrooms = total_mushrooms - spotted_mushrooms
    result = gilled_mushrooms
    return result

print(solution())