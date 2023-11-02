def solution():
    initial_brownies = 16
    percent_eaten_by_children = 25
    brownies_eaten_by_children = initial_brownies * (percent_eaten_by_children / 100)
    remaining_brownies = initial_brownies - brownies_eaten_by_children
    percent_eaten_by_family = 50
    brownies_eaten_by_family = remaining_brownies * (percent_eaten_by_family / 100)
    brownies_leftover = remaining_brownies - brownies_eaten_by_family - 1
    result = brownies_leftover
    return result

print(solution())