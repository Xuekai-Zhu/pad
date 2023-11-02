def solution():
    ounces_wax_car = 3
    ounces_wax_suv = 4
    ounces_spilt = 2
    ounces_left = 11 - ounces_spilt
    result = ounces_left - (ounces_wax_car + ounces_wax_suv)
    return result

print(solution())