def solution():
    """John buys 500 newspapers. Each newspaper sells for $2. He sells 80% of them. He buys them all for 75% less than the price at which he sells them. How much profit does he make?"""
    # Define the number of newspapers John buys and their selling price
    newspapers_bought = 500
    selling_price = 2

    # Calculate the number of newspapers sold and the total revenue
    newspapers_sold = newspapers_bought * 0.8
    total_revenue = newspapers_sold * selling_price

    # Calculate the cost of the newspapers purchased
    cost = total_revenue * 0.25

    # Calculate the profit
    profit = total_revenue - cost

    # Display the profit
    result = profit
    return result

print(solution())