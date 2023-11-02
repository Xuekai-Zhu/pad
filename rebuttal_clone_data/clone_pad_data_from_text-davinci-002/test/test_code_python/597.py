def solution():
    total_apartments = 120
    apartments_one_resident = total_apartments * 0.85
    apartments_two_residents = total_apartments * 0.60
    apartments_one_resident = apartments_one_resident - apartments_two_residents
    result = apartments_one_resident
    
    return result

print(solution())