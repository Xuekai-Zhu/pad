def solution():
    """John's camera broke so he decided to rent one for 4 weeks.  It was a $5000 camera and the rental fee was 10% of the value per week.  His friend who was there when it broke agreed to pay 40% of the rental fee.  How much did John pay?"""
    # Define the value of the camera and the rental fee percentage
    CAMERA_VALUE = 5000
    RENTAL_FEE_PERCENTAGE = 0.1

    # Define the number of weeks John rented the camera
    weeks_rented = 4

    # Calculate the rental fee for the camera
    rental_fee = CAMERA_VALUE * RENTAL_FEE_PERCENTAGE * weeks_rented

    # Calculate John's portion of the rental fee
    johns_fee = rental_fee * 0.6

    # Display John's fee
    result = johns_fee
    return result

print(solution())