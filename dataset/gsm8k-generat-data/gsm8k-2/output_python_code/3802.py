def solution():
    """Tom decides to buy some shirts from his favorite fandoms because there is a sale on his favorite website. He buys 5 t-shirts from each of his 4 favorite fandoms. The shirts normally cost $15 each but there is a 20% off sale. The order qualified for free shipping but he still needed to pay 10% tax. How much did he pay?"""
    num_fandoms = 4
    num_shirts = 5
    shirt_price = 15
    sale_percent = 20
    tax_percent = 10
    subtotal = num_fandoms * num_shirts * shirt_price * (1 - sale_percent/100)
    tax_amount = subtotal * (tax_percent/100)
    total = subtotal + tax_amount
    result = total
    return result

print(solution())