def solution():
    """John's camera broke so he decided to rent one for 4 weeks. It was a $5000 camera and the rental fee was 10% of the value per week. His friend who was there when it broke agreed to pay 40% of the rental fee. How much did John pay?"""
    camera_value = 5000
    rental_fee = camera_value * 0.1
    total_rental_fee = rental_fee * 4
    friend_payment = total_rental_fee * 0.4
    john_payment = total_rental_fee - friend_payment
    result = john_payment
    return result

print(solution())