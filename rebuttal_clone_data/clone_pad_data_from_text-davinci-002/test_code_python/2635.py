def solution():
    old_apartment_monthly_cost = 1200
    new_apartment_monthly_cost = old_apartment_monthly_cost * 1.4
    old_apartment_yearly_cost = old_apartment_monthly_cost * 12
    new_apartment_yearly_cost = new_apartment_monthly_cost * 12
    total_saved = old_apartment_yearly_cost - new_apartment_yearly_cost
    per_person_saved = total_saved / 3
    result = per_person_saved
    return result

print(solution())