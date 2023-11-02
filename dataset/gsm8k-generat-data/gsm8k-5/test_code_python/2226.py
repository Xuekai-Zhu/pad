def solution():
    sugar_used = 24  # Paul used 24 cups of sugar for the first week's recipe
    for i in range(3):  # Loop for the remaining 3 weeks
        sugar_used /= 2  # Reduce the amount of sugar by half each week
    result = sugar_used
    return result

print(solution())