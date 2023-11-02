def solution():
    num_baskets = 6
    strawberries_per_basket = 50
    num_friends = 3

    # Calculate the total number of strawberries that Lilibeth picks
    lilibeth_strawberries = num_baskets * strawberries_per_basket

    # Calculate the total number of strawberries that all of Lilibeth's friends pick
    friends_strawberries = lilibeth_strawberries * num_friends

    # Calculate the total number of strawberries that Lilibeth and her friends pick in all
    total_strawberries = lilibeth_strawberries + friends_strawberries
    result = total_strawberries
    return result

print(solution())