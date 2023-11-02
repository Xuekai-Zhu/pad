def solution():
    initial_payment = 500
    couch_price = 750
    table_price = 100
    lamp_price = 50

    # Calculate the total cost of all furniture items
    total_cost = couch_price + table_price + lamp_price

    # Calculate the amount still owed after the initial payment
    amount_owed = total_cost - initial_payment
    result = amount_owed
    return result

print(solution())