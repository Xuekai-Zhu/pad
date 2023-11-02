def solution():
    num_eggs_in_carton = 12
    num_emmys_won = 6
    if num_emmys_won >= num_eggs_in_carton:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())