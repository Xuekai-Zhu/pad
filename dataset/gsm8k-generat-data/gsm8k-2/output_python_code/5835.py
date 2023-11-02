def solution():
    """It takes 3 ounces of wax to detail Kellan’s car and 4 ounces to detail his SUV. He bought an 11-ounce bottle of vehicle wax, but spilled 2 ounces before using it. How many ounces does he have left after waxing his car and SUV?"""
    car_wax_amount = 3
    suv_wax_amount = 4
    total_wax_amount = 11 - 2  # subtracting spilled wax
    remaining_wax = total_wax_amount - (car_wax_amount + suv_wax_amount)
    result = remaining_wax
    return result

print(solution())