def solution():
    total_candies_bought = 3 + 5 + 2  # Total candies Susan bought during the week
    candies_left = 4  # Candies Susan had left at the end of the week
    candies_consumed = total_candies_bought - candies_left  # Candies Susan consumed during the week
    result = candies_consumed
    return result

print(solution())