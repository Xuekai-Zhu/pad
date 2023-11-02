def solution():
    # Find the total number of fruits in all the baskets
    total_fruits = 15 + 30 + 20 + 25  # the total fruits in A, B, C, and D baskets
    # Calculate the number of bananas in basket E
    bananas_in_E = (25*5 - total_fruits) / 5  # the average number of fruits per basket is 25, so the total fruits in 5 baskets is 125
    result = bananas_in_E
    return result

print(solution())