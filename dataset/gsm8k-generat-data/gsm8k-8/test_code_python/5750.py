def solution():
    # Calculate the total number of oranges Sophie received in 30 days
    oranges_per_day_sophie = 20
    total_oranges_sophie = oranges_per_day_sophie * 30

    # Calculate the total number of grapes Hannah received in 30 days
    grapes_per_day_hannah = 40
    total_grapes_hannah = grapes_per_day_hannah * 30

    # Calculate the total number of fruits both girls ate in 30 days
    total_fruits = total_oranges_sophie + total_grapes_hannah
    result = total_fruits
    return result

print(solution())