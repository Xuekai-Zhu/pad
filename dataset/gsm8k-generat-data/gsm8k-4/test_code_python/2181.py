def solution():
    """John's camera broke so he decided to rent one for 4 weeks. It was a $5000 camera and the rental fee was 10% of the value per week. His friend who was there when it broke agreed to pay 40% of the rental fee. How much did John pay?"""
    # Define the camera value and rental fee
    camera_value = 5000
    rental_fee = camera_value * 0.1

    # Calculate the total rental cost
    rental_cost = rental_fee * 4

    # Calculate John's portion of the rental cost
    john_cost = rental_cost * 0.6

    result = john_cost
    return result

print(solution())