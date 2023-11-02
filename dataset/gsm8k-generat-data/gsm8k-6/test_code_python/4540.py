def solution():
    # Calculate the total cups of food consumed by the dogs in a day
    total_cups = 1.5 * 2 * 3  # two dogs, 1.5 cups per meal, three meals a day
    
    # Convert cups to pounds
    total_pounds = total_cups / 2.25  # 1 pound is equal to 2.25 cups
    
    result = total_pounds
    return result

print(solution())