def solution():
    rental_cost_per_hour = 5  # The cottage rental cost is $5 per hour
    rental_duration = 8  # They rented the cottage for 8 hours
    total_rental_cost = rental_cost_per_hour * rental_duration  # Calculate the total rental cost

    # Calculate the amount each friend paid
    amount_per_friend = total_rental_cost / 2
    result = amount_per_friend
    return result

print(solution())