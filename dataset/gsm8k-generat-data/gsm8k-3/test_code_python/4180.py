def solution():
    """Maria buys a large bar of French soap that lasts her for 2 months.  She spends $8.00 per bar of soap.  If she wants to stock up for the entire year, how much will she spend on soap?"""
    # Calculate the number of bars of soap needed for the entire year
    bars_needed = 12 / 2  # 2 months per bar, 12 months in a year

    # Calculate the total cost of the soap for the entire year
    total_cost = bars_needed * 8  # $8.00 per bar of soap

    # Display the total cost
    result = total_cost
    return result

print(solution())