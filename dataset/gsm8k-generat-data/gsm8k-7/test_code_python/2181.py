def solution():
    camera_value = 5000
    rental_percent = 0.1
    rental_weeks = 4
    friend_percent = 0.4

    # Calculate the total rental fee for the 4 weeks
    rental_fee = camera_value * rental_percent * rental_weeks

    # Calculate the amount John's friend will pay
    friend_payment = rental_fee * friend_percent

    # Calculate the amount John will pay
    john_payment = rental_fee - friend_payment
    result = john_payment
    return result

print(solution())