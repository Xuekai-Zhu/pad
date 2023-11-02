def solution():
    total_cost = 1700  # The cost of the car is $1700
    num_friends = 6  # There are 6 friends planning to buy the car
    share_of_cost = total_cost / num_friends  # Each friend would have paid $283.33

    # Deduct the funds raised at the car wash from the total cost
    remaining_cost = total_cost - 500

    # Deduct Brad's share from the remaining cost
    remaining_cost -= share_of_cost

    # Calculate how much more each friend has to pay now that Brad isn't participating
    new_share_of_cost = remaining_cost / (num_friends - 1)

    # Calculate the difference in each friend's share of the cost
    diff_per_friend = new_share_of_cost - share_of_cost
    result = diff_per_friend
    return result

print(solution())