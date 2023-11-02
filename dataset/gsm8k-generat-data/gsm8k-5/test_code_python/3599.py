def solution():
    # Calculate the number of shrimp caught by Austin's trap
    austin_shrimp = 26 - 8

    # Calculate the total number of shrimp caught
    total_shrimp = 26 + austin_shrimp + ((26 + austin_shrimp)/2)

    # Calculate the earnings from selling the shrimp
    earnings = (total_shrimp // 11) * 7

    # Calculate the amount of money each boy makes
    individual_earnings = earnings / 3
    result = individual_earnings
    return result

print(solution())