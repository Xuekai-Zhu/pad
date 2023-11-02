def solution():
    # Define the cost of the furniture items
    couch_cost = 750
    table_cost = 100
    lamp_cost = 50

    # Define the amount of money Daria has saved to pay for the furniture
    saved_money = 500

    # Calculate the total cost of the furniture
    total_cost = couch_cost + table_cost + lamp_cost

    # Calculate the amount Daria still owes before interest
    amount_owed = total_cost - saved_money
    result = amount_owed
    return result

print(solution())