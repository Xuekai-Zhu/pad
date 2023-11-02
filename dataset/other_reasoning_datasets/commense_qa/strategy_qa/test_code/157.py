def solution():
    chick_fil_a_closed_on_sundays = True
    halloween_2021_is_on_sunday = True
    if chick_fil_a_closed_on_sundays and halloween_2021_is_on_sunday:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())