def solution():
    total_hours = 8
    total_coins = 100
    small_bags = 2
    big_bag_coins = total_coins
    small_bag_coins = big_bag_coins / 2
    total_coins = big_bag_coins + small_bag_coins
    coins_per_hour = total_coins / total_hours
    result = coins_per_hour
    return result

print(solution())