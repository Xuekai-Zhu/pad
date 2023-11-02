def solution():
    """Tom decides to buy some shirts from his favorite fandoms because there is a sale on his favorite website.  He buys 5 t-shirts from each of his 4 favorite fandoms.  The shirts normally cost $15 each but there is a 20% off sale.   The order qualified for free shipping but he still needed to pay 10% tax.  How much did he pay?"""
    # Define the regular price of each t-shirt
    regular_price = 15

    # Define the discount multiplier
    discount_multiplier = 0.2

    # Define the number of t-shirts purchased from each fandom
    tshirts_per_fandom = 5

    # Calculate the discounted price of each t-shirt
    discounted_price = regular_price * (1 - discount_multiplier)

    # Calculate the total cost of all the t-shirts
    total_cost = tshirts_per_fandom * 4 * discounted_price

    # Calculate the cost of the tax
    tax_cost = total_cost * 0.1

    # Calculate the total cost including tax
    total_cost += tax_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())