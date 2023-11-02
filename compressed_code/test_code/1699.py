def solution():
    
    camera_value = 5000
    rental_fee_per_week = camera_value * 0.1
    total_rental_fee = rental_fee_per_week * 4
    friend_share = total_rental_fee * 0.4
    john_share = total_rental_fee - friend_share
    result = john_share
    return result

print(solution())