def solution():
    """Bert has a garden shop. He buys his products in a warehouse and sells them for $10 more in his shop. From each sale, he has to pay 10% of the value in tax. One day a client came to his shop and bought a barrel for $90. How Much money did Bert make on this sale?"""
    # Define the cost of the product and the price it's sold for
    cost = 90
    price = 100

    # Calculate the profit
    profit = price - cost

    # Calculate the amount of tax to pay
    tax = price * 0.1

    # Calculate Bert's earnings after paying the tax
    earnings = profit - tax

    # return the result
    result = earnings
    return result

print(solution())