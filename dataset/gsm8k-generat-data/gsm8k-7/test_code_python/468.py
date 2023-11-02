def solution():
    num_tshirts = 6
    tshirt_price = 8

    num_sweaters = 4
    sweater_price = 18

    num_jackets = 5
    jacket_price = 80
    jacket_discount = 0.1  # 10% discount
    jacket_discounted_price = jacket_price * (1 - jacket_discount)

    sales_tax_rate = 0.05  # 5% sales tax rate

    # Calculate the total cost of all T-shirts
    total_tshirt_cost = num_tshirts * tshirt_price

    # Calculate the total cost of all sweaters
    total_sweater_cost = num_sweaters * sweater_price

    # Calculate the total cost of all jackets
    total_jacket_cost = num_jackets * jacket_discounted_price

    # Calculate the subtotal before sales tax
    subtotal = total_tshirt_cost + total_sweater_cost + total_jacket_cost

    # Calculate the sales tax
    sales_tax = subtotal * sales_tax_rate

    # Calculate the total cost including sales tax
    total_cost = subtotal + sales_tax
    result = total_cost
    return result

print(solution())