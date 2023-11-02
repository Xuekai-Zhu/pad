def solution():
    # Calculate the total number of pomelos in all boxes
    total_pomelos = 240 + 20 * 10

    # Calculate the total number of dozens of pomelos
    dozens_of_pomelos = total_pomelos // 12

    result = dozens_of_pomelos
    return result

print(solution())