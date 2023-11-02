def solution():
    """Bert has a garden shop. He buys his products in a warehouse and sells them for $10 more in his shop. From each sale, he has to pay 10% of the value in tax. One day a client came to his shop and bought a barrel for $90. How much money did Bert make on this sale?"""
    cost_price = 90
    selling_price = cost_price + 10
    tax_percent = 10
    tax_paid = (selling_price * tax_percent) / 100
    profit = selling_price - (cost_price + tax_paid)
    result = profit
    
    return result

print(solution())