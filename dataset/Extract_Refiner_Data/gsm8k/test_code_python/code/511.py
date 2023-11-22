def solution():
    
    # Define the cost of each pack of canvas bags and the selling price of each pack at the craft fair
    PACK_COST = 4
    CRAFT_FRIEND_PRICE = 8

    # Define the number of packs of canvas bags purchased and the number of packs sold at the craft fair
    PACKS_PURCHASED = 8
    PACKS_SOLD = PACKS_PURCHASED * 5

    # Calculate the total cost of the purchase
    total_cost = PACK_COST * PACKS_PURCHASED

    # Calculate the total revenue from selling the bags at the craft fair
    total_revenue = PACK_COST * PACKS_SOLD

    # Calculate the profit
    profit = total_revenue - total_cost

    # Display the profit
    result = profit
    return result

print(solution())