def solution():
    """Tom decides to buy some shirts from his favorite fandoms because there is a sale on his favorite website. He buys 5 t-shirts from each of his 4 favorite fandoms. The shirts normally cost $15 each but there is a 20% off sale. The order qualified for free shipping but he still needed to pay 10% tax. How much did he pay?"""
    # Define the number of t-shirts purchased from each fandom
    t_shirts_per_fandom = 5

    # Define the normal price of each t-shirt
    normal_price = 15

    # Calculate the sale price of each t-shirt
    sale_price = normal_price * (1 - 0.20)

    # Calculate the total cost of the t-shirts before tax
    subtotal = t_shirts_per_fandom * 4 * sale_price

    # Calculate the tax amount
    tax = subtotal * 0.10

    # Calculate the total cost of the order
    total_cost = subtotal + tax

    # return the result
    result = total_cost
    return result

print(solution())