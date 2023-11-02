def solution():
    base_price = 3
    price_per_mile = 4
    total_paid = 23

    # Calculate the total amount paid for the distance traveled
    distance_cost = total_paid - base_price

    # Calculate the distance traveled
    distance = distance_cost / price_per_mile
    result = distance
    return result

print(solution())