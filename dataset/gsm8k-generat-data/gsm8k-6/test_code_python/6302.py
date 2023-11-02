def solution():
    # Calculate the number of regular cars and trucks Pauline has
    regular_cars = 0.64 * 125
    trucks = 0.08 * 125
    
    # Calculate the number of convertibles Pauline has
    convertibles = 125 - regular_cars - trucks
    result = convertibles
    return result

print(solution())