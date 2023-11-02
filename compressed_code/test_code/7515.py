def solution():
    
    camera_value = 5000
    rental_fee = camera_value * 0.1
    total_rental_fee = rental_fee * 4
    friend_payment = total_rental_fee * 0.4
    john_payment = total_rental_fee - friend_payment
    result = john_payment
    return result

print(solution())