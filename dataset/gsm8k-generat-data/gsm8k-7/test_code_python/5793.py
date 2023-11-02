def solution():
    toy_price = 12.0
    num_toys = 4
    discount = 0.5  # 50% discount for the second toy in each pair

    # Determine how many full-priced toys and half-priced toys Samantha buys
    full_priced_toys = num_toys // 2  # integer division to get whole number of pairs
    half_priced_toys = num_toys - full_priced_toys

    # Calculate the total cost of all full-priced toys and half-priced toys
    total_cost = (full_priced_toys * toy_price) + (half_priced_toys * (toy_price * discount))

    result = total_cost
    return result

print(solution())