def solution():
    """It takes 3 ounces of wax to detail Kellan's car and 4 ounces to detail his SUV. He bought an 11-ounce bottle of vehicle wax, but spilled 2 ounces before using it. How many ounces does he have left after waxing his car and SUV?"""
    car_wax = 3
    suv_wax = 4
    total_wax_needed = car_wax + suv_wax
    wax_bottle_size = 11
    wax_spilled = 2
    wax_remaining = wax_bottle_size - wax_spilled
    wax_used = total_wax_needed
    wax_leftover = wax_remaining - wax_used
    result = wax_leftover
    return result

print(solution())