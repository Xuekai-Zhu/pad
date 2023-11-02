def solution():
    """Martin eats 1/2 cup of berries every day. The grocery store is selling a package of berries (1 cup per pack) for $2.00. How much will he spend on berries in a 30 day period?"""
    # Define the amount of berries Martin eats every day and the size of each pack
    daily_amount = 0.5
    pack_size = 1

    # Calculate the number of packs Martin needs to buy in 30 days
    packs_needed = daily_amount * 30 / pack_size

    # Calculate the total cost of the berries
    total_cost = packs_needed * 2.0

    result = total_cost
    return result

print(solution())