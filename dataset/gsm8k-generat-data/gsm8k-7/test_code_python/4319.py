def solution():
    num_trees = 10
    oranges_per_day = 12
    pack_size = 6
    pack_price = 2
    num_days = 21

    # Calculate the total number of oranges that Tammy can pick
    total_oranges = num_trees * oranges_per_day * num_days

    # Calculate the total number of 6-packs of oranges that Tammy can sell
    total_packs = total_oranges // pack_size

    # Calculate the total amount of money that Tammy will earn
    total_earnings = total_packs * pack_price
    result = total_earnings
    return result

print(solution())