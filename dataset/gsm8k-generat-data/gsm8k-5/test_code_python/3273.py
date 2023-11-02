def solution():
    cost_per_bag = 0.5  # It costs $.5 for a bag with 100 seeds
    seeds_per_ear = 4  # For every 4 seeds planted, the farmer gets one ear
    price_per_ear = 0.1  # The farmer can sell one ear for $.1
    profit_goal = 40  # The farmer wants to make $40 in profit

    # Calculate the number of bags of seeds the farmer needs to buy
    bags_needed = profit_goal / price_per_ear / seeds_per_ear * 100

    # Round up to the nearest whole number of bags
    bags_needed = int(bags_needed + 1)

    # Calculate the cost of buying the needed number of bags
    total_cost = bags_needed * cost_per_bag

    # Calculate the number of ears the farmer can sell from the seeds he plants
    ears_produced = bags_needed * 100 // seeds_per_ear

    # Calculate the profit the farmer makes from selling the ears of corn
    total_profit = ears_produced * price_per_ear

    # Calculate the number of ears sold by the farmer
    ears_sold = (total_profit - total_cost) // price_per_ear
    result = ears_sold
    return result

print(solution())