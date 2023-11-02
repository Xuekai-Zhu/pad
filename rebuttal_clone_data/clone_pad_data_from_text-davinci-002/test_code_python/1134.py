def solution():
    lollipops_eaten_per_day = 45
    henrys_lollipops = 60 + 30
    alisons_lollipops = 60
    dianes_lollipops = 2 * alisons_lollipops
    total_lollipops = henrys_lollipops + alisons_lollipops + dianes_lollipops
    days_to_finish = total_lollipops / lollipops_eaten_per_day
    result = days_to_finish
    return result

print(solution())