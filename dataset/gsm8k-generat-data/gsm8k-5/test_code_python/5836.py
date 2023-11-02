def solution():
    wax_per_car = 3  # It takes 3 ounces of wax to detail Kellan's car
    wax_per_suv = 4  # It takes 4 ounces of wax to detail Kellan's SUV
    wax_total = 11  # Kellan bought an 11-ounce bottle of vehicle wax
    wax_spilled = 2  # Kellan spilled 2 ounces before using the wax

    # Calculate the amount of wax used on the car and SUV
    wax_used = wax_per_car + wax_per_suv

    # Calculate the amount of wax left after detailing
    wax_left = wax_total - wax_spilled - wax_used
    result = wax_left
    return result

print(solution())