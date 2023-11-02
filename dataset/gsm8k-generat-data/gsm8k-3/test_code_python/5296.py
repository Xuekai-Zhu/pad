def solution():
    """Bob orders a dozen muffins a day for $0.75 each and sells them for $1.5 each.  How much profit does he make a week?"""
    # Define the cost and selling price of a single muffin
    COST_PER_MUFFIN = 0.75
    SELLING_PRICE_PER_MUFFIN = 1.5

    # Calculate the profit per dozen muffins
    profit_per_dozen = (SELLING_PRICE_PER_MUFFIN - COST_PER_MUFFIN) * 12

    # Calculate the profit per day
    profit_per_day = profit_per_dozen * 1

    # Calculate the profit per week
    profit_per_week = profit_per_day * 7

    # Display the profit per week
    result = profit_per_week
    return result

print(solution())