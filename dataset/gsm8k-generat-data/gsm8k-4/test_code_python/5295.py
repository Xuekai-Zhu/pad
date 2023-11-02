def solution():
    """Jack orders 3 sandwiches that cost $5 each. He pays with a $20 bill. How much does he get in change?"""
    # Define the cost of each sandwich and the amount paid by Jack
    sandwich_cost = 5
    amount_paid = 20

    # Calculate the total cost of the sandwiches
    total_cost = sandwich_cost * 3

    # Calculate the amount of change Jack should receive
    change = amount_paid - total_cost

    result = change
    return result

print(solution())