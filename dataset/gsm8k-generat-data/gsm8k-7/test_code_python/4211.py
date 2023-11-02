def solution():
    total_fruits = (15 + 30 + 20 + 25)  # total fruits in baskets A, B, C, and D
    num_baskets = 5
    average_fruits_per_basket = 25

    # Calculate the total number of fruits in all five baskets
    total_fruits_in_all_baskets = num_baskets * average_fruits_per_basket

    # Calculate the number of bananas in basket E
    bananas_in_e = total_fruits_in_all_baskets - total_fruits
    result = bananas_in_e
    return result

print(solution())