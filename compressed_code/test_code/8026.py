def solution():
    
    pounds_of_beef = 15
    ounces_of_beef = pounds_of_beef * 16
    ounces_per_steak = 12
    total_steaks = ounces_of_beef / ounces_per_steak
    result = total_steaks
    return result

print(solution())