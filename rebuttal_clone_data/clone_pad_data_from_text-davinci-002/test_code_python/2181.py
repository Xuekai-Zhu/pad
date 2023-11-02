def solution():
    camera_cost = 5000
    rental_fee_percentage = 10
    rental_fee = camera_cost * (rental_fee_percentage / 100)
    weeks_rented = 4
    friend_contribution = rental_fee * 0.4
    johns_payment = rental_fee - friend_contribution
    result = johns_payment
    return result

print(solution())