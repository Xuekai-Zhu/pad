def solution():
    lilibeth_baskets = 6  # Lilibeth fills 6 baskets
    friends = 3  # Three of Lilibeth's friends pick the same amount as her
    strawberries_per_basket = 50  # Each basket holds 50 strawberries

    # Calculate the total number of strawberries picked by Lilibeth and her friends
    total_strawberries = (lilibeth_baskets + (lilibeth_baskets * friends)) * strawberries_per_basket

    result = total_strawberries
    return result

print(solution())