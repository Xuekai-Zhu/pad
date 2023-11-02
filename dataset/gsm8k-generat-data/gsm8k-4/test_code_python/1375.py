def solution():
    """A farmer owns a hog that recently gave birth to 6 piglets. If the farmer raises the piglets until they are fully grown, he can sell the fully grown pig for $300. Each piglet must grow for at least 12 months before it is large enough to be sold. It costs the farmer $10 per month to feed each animal until it is sold. If the farmer sells 3 pigs after 12 months, and the remaining 3 pigs after 16 months, how much profit did he earn in total (after deducting the cost of food)?"""
    # Define the cost to feed each piglet per month and the selling price of a fully grown pig
    cost_per_month = 10
    selling_price = 300

    # Define the number of pigs to be sold after 12 and 16 months
    pigs_sold_12_months = 3
    pigs_sold_16_months = 3

    # Calculate the total cost to feed each piglet for 16 months before they are sold
    total_cost = (12 + 16) * cost_per_month * 6

    # Calculate the revenue from selling the fully grown pigs
    revenue = (pigs_sold_12_months + pigs_sold_16_months) * selling_price

    # Calculate the total profit
    profit = revenue - total_cost

    # Return the result
    result = profit
    return result

print(solution())