def solution():
    brownies = 20
    brownies_to_admin = brownies // 2
    brownies_left = brownies - brownies_to_admin
    brownies_to_carl = brownies_left // 2
    brownies_left -= brownies_to_carl
    brownies_left -= 2  # two brownies went to Simon
    result = brownies_left
    return result

print(solution())