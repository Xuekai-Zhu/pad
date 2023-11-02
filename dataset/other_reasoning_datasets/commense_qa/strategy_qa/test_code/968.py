def solution():
    us_presidents_1800s = 24
    unlucky_numbers = [4, 13]
    if us_presidents_1800s not in unlucky_numbers:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())