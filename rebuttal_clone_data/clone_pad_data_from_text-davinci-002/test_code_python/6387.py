def solution():
    floor_length = 10
    floor_width = 8
    carpet_length = 4
    carpet_area = carpet_length ** 2
    number_of_carpets = (floor_length * floor_width) / carpet_area
    number_of_carpets_rounded = round(number_of_carpets)
    number_of_carpets_remaining = number_of_carpets_rounded - number_of_carpets
    uncovered_area = number_of_carpets_remaining * carpet_area
    result = uncovered_area
    return result

print(solution())