def solution():
    """Jack and Jill are friends who borrow from each other often. Last week Jack borrowed  $1200 from Jill, which he promised to pay back with an interest of 10%. How much will Jack pay back?"""
    # Define the amount borrowed and the interest rate
    borrowed_amount = 1200
    interest_rate = 0.1

    # Calculate the amount of interest
    interest_amount = borrowed_amount * interest_rate

    # Calculate the total amount to be paid back
    total_amount = borrowed_amount + interest_amount

    # Display the total amount to be paid back
    result = total_amount
    return result

print(solution())