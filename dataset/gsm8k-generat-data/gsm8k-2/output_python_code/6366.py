def solution():
    """Bert has a garden shop. He buys his products in a warehouse and sells them for $10 more in his shop. From each sale, he has to pay 10% of the value in tax. One day a client came to his shop and bought a barrel for $90. How Much money did Bert make on this sale?"""
    warehouse_price = 90
    selling_price = warehouse_price + 10
    tax = selling_price * 0.1
    profit = selling_price - warehouse_price - tax
    result = profit
    return result

print(solution())