def solution():
    num_horses = 4
    oats_per_horse_per_meal = 5
    num_meals_per_day = 2
    oats_per_bag = 50
    num_days = 5

    # Calculate the total amount of oats consumed per day
    total_oats_per_day = num_horses * oats_per_horse_per_meal * num_meals_per_day

    # Calculate the total amount of oats needed per day
    total_oats_per_day = total_oats_per_day * num_days

    # Calculate the total amount of oats needed for all bags
    total_oats_for_bags = total_oats_per_day / oats_per_bag
    result = total_oats_for_bags
    return result

print(solution())