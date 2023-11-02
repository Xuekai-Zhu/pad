def solution():
    old_rent = 2
    old_apartment_size = 750
    old_monthly_rent = old_rent * old_apartment_size
    new_monthly_rent = 2800
    rent_difference = old_monthly_rent - new_monthly_rent
    rent_saved_monthly = rent_difference / 2
    rent_saved_yearly = rent_saved_monthly * 12
    result = rent_saved_yearly
    return result

print(solution())