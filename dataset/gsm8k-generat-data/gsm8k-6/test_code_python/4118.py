def solution():
    # Calculate the total number of servings in 3 pies
    total_servings = 3 * 8  

    # Calculate the total number of apples needed for all servings
    total_apples = total_servings * 1.5

    # Calculate the average number of apples per guest
    avg_apples = total_apples / 12
    result = avg_apples
    return result

print(solution())