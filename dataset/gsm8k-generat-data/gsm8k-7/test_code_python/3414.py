def solution():
    num_baskets_per_week = 3
    num_crabs_per_basket = 4
    num_collections_per_week = 2
    price_per_crab = 3

    # Calculate the total number of crabs collected in a week
    total_crabs_per_week = num_baskets_per_week * num_crabs_per_basket

    # Calculate the total number of crabs collected in all collections
    total_crabs = total_crabs_per_week * num_collections_per_week

    # Calculate the total money made from selling all crabs
    total_money = total_crabs * price_per_crab
    result = total_money
    return result

print(solution())