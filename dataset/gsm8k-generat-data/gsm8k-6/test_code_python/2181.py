def solution():
    camera_value = 5000  # value of the camera
    rental_fee = camera_value * 0.1  # rental fee per week
    rental_fee_total = rental_fee * 4  # total rental fee for 4 weeks
    friend_payment = 0.4 * rental_fee_total  # friend's payment towards the rental fee
    john_payment = rental_fee_total - friend_payment  # John's payment towards the rental fee
    result = john_payment
    return result

print(solution())