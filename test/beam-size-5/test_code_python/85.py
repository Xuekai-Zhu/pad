def solution():
    gift_bags_per_guest = 0.75  # Christina needs 0.75 gift bags per invited guest
    num_friends = 16  # Christina invited 16 friends
    gift_bags_needed = num_friends * gift_bags_per_guest  # Calculate the number of gift bags needed

    # Calculate the total number of gift bags needed
    total_gift_bags_needed = num_friends * gift_bags_needed

    # Calculate the total cost of the gift bags
    total_cost = total_gift_bags_needed * 2
    result = total_cost
    return result

print(solution())