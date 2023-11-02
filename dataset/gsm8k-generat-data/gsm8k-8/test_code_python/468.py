def solution():
    # Define the prices and quantities of each item
    tshirt_price = 8
    sweater_price = 18
    jacket_price = 80
    jacket_discount = 0.1
    sales_tax = 0.05
    tshirt_quantity = 6
    sweater_quantity = 4
    jacket_quantity = 5

    # Calculate the total price of each item type
    tshirt_total_price = tshirt_price * tshirt_quantity
    sweater_total_price = sweater_price * sweater_quantity
    jacket_total_price = (1 - jacket_discount) * jacket_price * jacket_quantity

    # Calculate the subtotal before tax
    subtotal = tshirt_total_price + sweater_total_price + jacket_total_price

    # Calculate the total price including tax
    total_price = subtotal * (1 + sales_tax)

    result = total_price
    return result

print(solution())