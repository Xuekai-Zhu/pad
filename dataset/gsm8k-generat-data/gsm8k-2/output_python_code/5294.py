def solution():
    """Jack orders 3 sandwiches that cost $5 each. He pays with a $20 bill. How much does he get in change?"""
    sandwich_cost = 5
    num_sandwiches = 3
    total_cost = sandwich_cost * num_sandwiches
    payment = 20
    change = payment - total_cost
    result = change
    return result

print(solution())