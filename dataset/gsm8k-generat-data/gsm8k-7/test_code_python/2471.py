def solution():
    num_nights = 3
    cost_per_night = 250
    discount = 100

    # Calculate the total cost of the hotel room without discount
    total_cost = num_nights * cost_per_night

    # Calculate the discounted cost
    discounted_cost = total_cost - discount

    result = discounted_cost
    return result

print(solution())