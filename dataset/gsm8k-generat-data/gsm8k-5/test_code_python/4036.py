def solution():
    cakes_on_sixth_day = 320  # Marjorie makes 320 cakes on the sixth day
    cakes_on_fifth_day = cakes_on_sixth_day / 2  # Marjorie makes half as many cakes on the fifth day
    cakes_on_fourth_day = cakes_on_fifth_day / 2  # Marjorie makes half as many cakes on the fourth day
    cakes_on_third_day = cakes_on_fourth_day / 2  # Marjorie makes half as many cakes on the third day
    cakes_on_second_day = cakes_on_third_day / 2  # Marjorie makes half as many cakes on the second day
    cakes_on_first_day = cakes_on_second_day / 2  # Marjorie makes half as many cakes on the first day

    result = cakes_on_first_day
    return result

print(solution())