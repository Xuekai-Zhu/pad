def solution():
    # Calculate the total number of fruits in all baskets
    total_fruits = 5 * 25

    # Calculate the total number of fruits in A, B, C, and D baskets
    total_ABDC_fruits = 15 + 30 + 20 + 25

    # Calculate the number of bananas in basket E
    bananas_in_E = total_fruits - total_ABDC_fruits

    result = bananas_in_E
    return result

print(solution())