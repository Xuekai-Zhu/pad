def solution():
    """Lilibeth and her friends go strawberry picking. Lilibeth fills 6 baskets where each basket holds 50 strawberries. If three of Lilibeth's friends pick the same amount as her, how many strawberries do Lilibeth and her friends pick in all?"""
    # Define the number of baskets Lilibeth filled
    lilibeth_baskets = 6

    # Define the number of strawberries per basket
    strawberries_per_basket = 50

    # Calculate the total number of strawberries picked by Lilibeth
    lilibeth_strawberries = lilibeth_baskets * strawberries_per_basket

    # Calculate the total number of strawberries picked by Lilibeth and her friends
    total_strawberries = (lilibeth_strawberries + (lilibeth_strawberries * 3))

    # Display the total number of strawberries
    result = total_strawberries
    return result

print(solution())