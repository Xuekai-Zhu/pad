def solution():
    # Calculate the profit from fixing bike tires
    profit_tires = (20 - 5) * 300  # ($20 charged for tire repair - $5 parts cost) * 300 repairs

    # Calculate the profit from the complex repairs
    profit_complex = (300 - 50) * 2  # ($300 charged for complex repair - $50 parts cost) * 2 repairs

    # Calculate the profit from retail sales
    profit_sales = 2000

    # Calculate the total profit
    total_profit = profit_tires + profit_complex + profit_sales - 4000  # Subtract fixed expenses of $4000

    result = total_profit
    return result

print(solution())