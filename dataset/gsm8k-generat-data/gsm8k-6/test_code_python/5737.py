def solution():
    # Calculate the total number of candies needed
    total_candies = 20 + 4  # Paula needs to buy 4 additional candies

    # Calculate the number of candies each friend will get
    candies_per_friend = total_candies // 6  # // operator performs integer division

    result = candies_per_friend
    return result

print(solution())