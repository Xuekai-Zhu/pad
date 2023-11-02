def solution():
    cost_first_100_channels = 100  # The first 100 channels cost $100
    cost_next_100_channels = 100 / 2  # The next 100 channels cost half as much as the first 100
    total_cost = cost_first_100_channels + cost_next_100_channels  # Total cost for James without splitting

    # Calculate the amount James pays after splitting with his roommate
    amount_paid = total_cost / 2
    result = amount_paid
    return result

print(solution())