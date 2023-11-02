def solution():
    total_candies = 20
    num_friends = 6
    extra_candies = 4

    # Calculate the total number of candies needed
    total_candies_needed = (num_friends + 1) * (total_candies + extra_candies) / num_friends

    # Calculate the number of candies each friend will get
    num_candies_each = total_candies_needed / (num_friends + 1)
    result = num_candies_each
    return result

print(solution())