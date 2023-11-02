def solution():
    # Define the prices of each item
    spam_price = 3
    pb_price = 5
    bread_price = 2

    # Define the quantities of each item
    spam_qty = 12
    pb_qty = 3
    bread_qty = 4

    # Calculate the total cost of each item
    spam_total_cost = spam_price * spam_qty
    pb_total_cost = pb_price * pb_qty
    bread_total_cost = bread_price * bread_qty

    # Calculate the total amount paid
    total_amount = spam_total_cost + pb_total_cost + bread_total_cost
    result = total_amount
    return result

print(solution())