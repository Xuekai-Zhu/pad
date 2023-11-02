def solution():
    
    years_to_save = 3
    total_amount = 108000
    months_to_save = years_to_save * 12
    total_savings_per_month = total_amount / months_to_save
    savings_per_person_per_month = total_savings_per_month / 2
    result = savings_per_person_per_month
    return result

print(solution())