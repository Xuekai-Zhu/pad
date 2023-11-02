def solution():
    """A shopping center sells T-shirts at $8 each, a sweater at $18,  and a jacket at $80. The jacket is on sale with a 10% discount. The sales tax is 5%.  Kevin wants to buy six T-shirts, four sweaters, and five jackets for his children. How much does Kevin have to pay for all the items, including the sales tax?"""
    # Define the prices of each item
    T_SHIRT_PRICE = 8
    SWEATER_PRICE = 18
    JACKET_PRICE = 80

    # Define the discount on the jacket
    JACKET_DISCOUNT = 0.1

    # Define the sales tax rate
    SALES_TAX_RATE = 0.05

    # Define the quantities of each item purchased
    t_shirts = 6
    sweaters = 4
    jackets = 5

    # Calculate the cost of each item before discount and tax
    t_shirt_cost = t_shirts * T_SHIRT_PRICE
    sweater_cost = sweaters * SWEATER_PRICE
    jacket_cost = (1 - JACKET_DISCOUNT) * JACKET_PRICE * jackets

    # Calculate the total cost before tax
    total_cost_before_tax = t_shirt_cost + sweater_cost + jacket_cost

    # Calculate the sales tax
    sales_tax = total_cost_before_tax * SALES_TAX_RATE

    # Calculate the total cost including tax
    total_cost = total_cost_before_tax + sales_tax

    # Display the total cost
    result = total_cost
    return result

print(solution())