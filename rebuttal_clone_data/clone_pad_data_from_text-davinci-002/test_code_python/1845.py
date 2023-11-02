def solution():
    rock_roll_cds = 4
    pop_cds = 4
    dance_cds = 4
    country_cds = 4
    total_cds = rock_roll_cds + pop_cds + dance_cds + country_cds
    cost_of_cds = total_cds * 75
    money_needed = cost_of_cds - 75
    result = money_needed
    return result

print(solution())