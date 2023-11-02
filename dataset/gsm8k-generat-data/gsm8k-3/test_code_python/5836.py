def solution():
    """It takes 3 ounces of wax to detail Kellan’s car and 4 ounces to detail his SUV. He bought an 11-ounce bottle of vehicle wax, but spilled 2 ounces before using it. How many ounces does he have left after waxing his car and SUV?"""
    # Define the amount of wax needed for each vehicle
    CAR_WAX = 3
    SUV_WAX = 4

    # Define the total amount of wax in the bottle
    TOTAL_WAX = 11

    # Define the amount of wax spilled
    SPILLED_WAX = 2

    # Calculate the amount of wax used
    wax_used = CAR_WAX + SUV_WAX

    # Calculate the amount of wax remaining
    wax_remaining = TOTAL_WAX - SPILLED_WAX - wax_used

    # Display the amount of wax remaining
    result = wax_remaining
    return result

print(solution())