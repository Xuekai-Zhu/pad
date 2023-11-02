def solution():
    """Bert has a garden shop. He buys his products in a warehouse and sells them for $10 more in his shop.
    From each sale, he has to pay 10% of the value in tax. One day a client came to his shop and bought
    a barrel for $90. How much money did Bert make on this sale?"""
    # Define the price Bert paid for the barrel
    WAREHOUSE_PRICE = 80

    # Calculate the profit Bert made on the sale
    profit = (90 - WAREHOUSE_PRICE - 10) * 0.9

    # Display Bert's profit
    result = profit
    return result

print(solution())