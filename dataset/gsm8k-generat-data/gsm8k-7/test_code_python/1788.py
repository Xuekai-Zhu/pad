def solution():
    lychees_in_carton = 500
    sold_lychees = lychees_in_carton / 2
    remaining_lychees = sold_lychees * (2/5)
    eaten_lychees = remaining_lychees * (3/5)
    num_lychees_remaining = remaining_lychees - eaten_lychees
    result = num_lychees_remaining
    return result

print(solution())