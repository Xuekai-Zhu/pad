def solution():
    woodburning_sold = 20  # John sells 20 woodburning
    price_per_woodburning = 15  # John sells each woodburning for $15
    cost_of_wood = 100  # The wood cost $100

    # Calculate the total revenue from selling woodburning
    revenue = woodburning_sold * price_per_woodburning

    # Calculate the profit
    profit = revenue - cost_of_wood
    result = profit
    return result

print(solution())