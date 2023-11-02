def solution():
    # Calculate the number of ears of corn the farmer can get from one bag of seeds
    ears_per_bag = 100 // 4  # for every 4 seeds he plants, he gets one ear of corn

    # Calculate the profit per bag
    profit_per_bag = (ears_per_bag * 0.1) - 0.5  # he can sell each ear of corn for $.1, but it costs him $.5 for a bag of seeds

    # Calculate the number of bags of seeds the farmer needs to sell to make $40 in profit
    bags_needed = 40 // profit_per_bag

    # Calculate the number of ears of corn the farmer sold
    ears_sold = bags_needed * ears_per_bag

    result = ears_sold
    return result

print(solution())