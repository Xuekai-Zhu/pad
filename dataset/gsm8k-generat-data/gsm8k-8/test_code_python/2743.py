def solution():
    # Calculate the original retail value of all items
    retail_value = 2000 * 50

    # Calculate the discounted price of each item and the total revenue from the sale
    discount_price = 0.2 * 50
    sale_revenue = 0.9 * 2000 * (50 - discount_price)

    # Calculate the amount to pay back to creditors
    creditor_payment = 15000

    # Calculate the remaining money after paying back creditors
    remaining_money = sale_revenue - creditor_payment
    result = remaining_money
    return result

print(solution())