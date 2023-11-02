def solution():
    """It takes 3 ounces of wax to detail Kellan’s car and 4 ounces to detail his SUV. He bought an 11-ounce bottle of vehicle wax, but spilled 2 ounces before using it. How many ounces does he have left after waxing his car and SUV?"""
    # Define the amount of wax needed for detailing Kellan's car and SUV
    car_wax = 3
    suv_wax = 4

    # Define the amount of wax in the bottle after the spill
    bottle_wax = 11 - 2

    # Calculate the total amount of wax needed for detailing both vehicles
    total_wax = car_wax + suv_wax

    # Calculate the amount of wax left after detailing both vehicles
    wax_left = bottle_wax - total_wax

    # return the result
    result = wax_left
    return result

print(solution())