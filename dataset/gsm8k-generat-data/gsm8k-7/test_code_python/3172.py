def solution():
    num_friends = 3
    total_price = 15  # 3 friends paying $5 each
    num_bags = 5

    # Calculate the cost of each bag of chips
    cost_per_bag = total_price / (num_friends * num_bags)
    result = cost_per_bag
    return result

print(solution())