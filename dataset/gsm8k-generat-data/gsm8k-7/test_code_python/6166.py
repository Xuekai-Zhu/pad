def solution():
    num_baskets = 3
    num_strawberries_per_basket = 900
    remaining_fraction = 2/9
    
    # Calculate the total number of strawberries that were originally in the baskets
    total_strawberries = num_baskets * num_strawberries_per_basket
    
    # Calculate the number of strawberries that were eaten by each hedgehog
    num_strawberries_per_hedgehog = (total_strawberries * (1 - remaining_fraction)) / 2
    result = num_strawberries_per_hedgehog
    return result

print(solution())