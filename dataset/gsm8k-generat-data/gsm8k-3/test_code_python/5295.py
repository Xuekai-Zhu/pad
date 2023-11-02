def solution():
    """Jack orders 3 sandwiches that cost $5 each. He pays with a $20 bill. How much does he get in change?"""
    # Define the cost of one sandwich and the amount paid
    SANDWICH_COST = 5
    AMOUNT_PAID = 20

    # Calculate the total cost of the sandwiches
    total_cost = SANDWICH_COST * 3

    # Calculate the amount of change Jack gets back
    change = AMOUNT_PAID - total_cost

    # Display the amount of change
    result = change
    return result

print(solution())