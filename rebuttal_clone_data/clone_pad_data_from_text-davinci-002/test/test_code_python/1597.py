def solution():
    pounds_of_beef = 15
    ounces_per_pound = 16
    ounces_per_steak = 12
    total_ounces = pounds_of_beef * ounces_per_pound
    number_of_steaks = total_ounces / ounces_per_steak
    result = number_of_steaks
    return result

print(solution())