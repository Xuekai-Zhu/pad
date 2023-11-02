def solution():
    soup_weight = 80  # initial weight of the soup
    fourth_day_weight = soup_weight / (2**4)  # reduced by half for each day
    result = fourth_day_weight
    return result

print(solution())