def solution():
    # Calculate the total number of candies Susan bought
    total_bought = 3 + 5 + 2 + 4  # She bought 3 on Tuesday, 5 on Thursday, 2 on Friday, and has 4 left

    # Calculate the number of candies Susan ate
    candies_consumed = total_bought - 4  # She has 4 left, so she ate the difference

    result = candies_consumed
    return result

print(solution())