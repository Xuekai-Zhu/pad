def solution():
    area_of_one_blanket = 8*8
    total_area = 48
    number_of_blankets = 3
    area_of_blankets = number_of_blankets*area_of_one_blanket
    folds = area_of_blankets/total_area
    result = folds
    return result

print(solution())