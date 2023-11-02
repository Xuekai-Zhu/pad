def solution():
    # Define the amount of wax needed for Kellan's car and SUV
    car_wax = 3
    suv_wax = 4

    # Define the total amount of wax in the bottle and the amount spilled
    total_wax = 11
    spilled_wax = 2

    # Calculate the amount of wax used for Kellan's car and SUV
    used_wax = car_wax + suv_wax

    # Calculate the amount of wax left in the bottle
    remaining_wax = total_wax - spilled_wax - used_wax
    result = remaining_wax
    return result

print(solution())