def solution():
    camera_value = 5000  # The value of the camera was $5000
    rental_fee = camera_value * 0.1  # The rental fee was 10% of the camera value per week
    weeks = 4  # John rented the camera for 4 weeks
    total_rental_fee = rental_fee * weeks  # Calculate the total rental fee for 4 weeks
    friend_contribution = total_rental_fee * 0.4  # John's friend agreed to pay 40% of the rental fee
    john_payment = total_rental_fee - friend_contribution  # Calculate how much John needs to pay

    result = john_payment
    return result

print(solution())