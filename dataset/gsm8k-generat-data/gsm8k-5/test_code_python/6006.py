def solution():
    tabs_opened = 400
    tabs_closed_first_time = tabs_opened / 4  # Jose closed 1/4 of the tabs after an hour
    tabs_remaining = tabs_opened - tabs_closed_first_time  # Jose has this many tabs remaining after closing 1/4 of them
    tabs_closed_second_time = (2 / 5) * tabs_remaining  # Jose closed 2/5 of the remaining tabs after reading some news
    tabs_remaining = tabs_remaining - tabs_closed_second_time  # Jose has this many tabs remaining after closing 2/5 of the remaining tabs
    tabs_closed_third_time = tabs_remaining / 2  # Jose closed half of the remaining tabs after analyzing some pages
    tabs_remaining = tabs_remaining - tabs_closed_third_time  # Jose has this many tabs remaining after closing half of the remaining tabs
    result = tabs_remaining
    return result

print(solution())