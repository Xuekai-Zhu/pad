def solution():
    """You start a business selling charm bracelets. You spend $1 on the string for each bracelet and $3 on beads for each bracelet. You sell the bracelets for $6 each. If you sell 25 bracelets, how much profit will you make?"""
    # Define the cost and price of each bracelet
    cost_per_bracelet = 1 + 3
    price_per_bracelet = 6

    # Calculate the profit per bracelet
    profit_per_bracelet = price_per_bracelet - cost_per_bracelet

    # Calculate the total profit for selling 25 bracelets
    total_profit = profit_per_bracelet * 25

    result = total_profit
    return result

print(solution())