def solution():
    leesburg_pop = 58940  # Leesburg has 58940 people
    salem_size_ratio = 15  # Salem is 15 times the size of Leesburg
    salem_pop = leesburg_pop * salem_size_ratio  # Salem has 15 times the population of Leesburg
    salem_pop_after_move = salem_pop - 130000  # 130000 people move out of Salem
    salem_women_pop = salem_pop_after_move / 2  # Half of Salem's population is women
    result = salem_women_pop
    return result

print(solution())