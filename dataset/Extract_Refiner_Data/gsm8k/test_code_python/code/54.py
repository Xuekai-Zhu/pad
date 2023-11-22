def solution():
    
    # Define the initial bill and the delivery fees
    initial_bill = 40.00
    delivery_fees = initial_bill * 0.25

    # Calculate the total cost of the groceries
    total_cost = initial_bill + delivery_fees + 3.00 + 4.00

    # return the result
    result = total_cost
    return result

print(solution())