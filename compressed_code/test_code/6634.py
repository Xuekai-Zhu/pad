def solution():
    
    maize_per_month = 1
    months_in_two_years = 24
    total_maize = maize_per_month * months_in_two_years
    maize_stolen = 5
    maize_donated = 8
    final_maize = total_maize - maize_stolen + maize_donated
    result = final_maize
    return result

print(solution())