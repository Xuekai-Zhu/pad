def solution():
    seeds_per_bag = 100
    cost_per_bag = 0.5
    sale_price_per_ear = 0.1
    profit = 40

    # Calculate the number of bags of seeds the farmer bought
    num_bags = profit / (seeds_per_bag * cost_per_bag)

    # Calculate the number of seeds planted
    num_seeds_planted = num_bags * seeds_per_bag

    # Calculate the number of ears of corn harvested
    num_ears_harvested = num_seeds_planted // 4

    # Calculate the total profit from selling the ears of corn
    total_profit = num_ears_harvested * sale_price_per_ear

    result = num_ears_harvested
    return result

print(solution())