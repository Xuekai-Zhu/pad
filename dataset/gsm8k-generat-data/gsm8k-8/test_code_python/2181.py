def solution():
    # Define the given information
    camera_value = 5000
    rental_fee = 0.1 * camera_value
    rental_duration = 4
    friend_contribution = 0.4

    # Calculate John's total rental fee
    total_rental_fee = rental_fee * rental_duration

    # Calculate the friend's contribution
    friend_amount = friend_contribution * total_rental_fee

    # Calculate John's total cost
    john_cost = total_rental_fee - friend_amount
    result = john_cost
    return result

print(solution())