def solution():
    rooms_on_first_floor = 3
    rooms_on_second_floor = 3
    rooms_on_third_floor = 2
    monthly_rent_first_floor = rooms_on_first_floor * 15
    monthly_rent_second_floor = rooms_on_second_floor * 20
    monthly_rent_third_floor = rooms_on_third_floor * (2 * 15)
    total_monthly_rent = monthly_rent_first_floor + monthly_rent_second_floor + monthly_rent_third_floor
    result = total_monthly_rent
    return result

print(solution())