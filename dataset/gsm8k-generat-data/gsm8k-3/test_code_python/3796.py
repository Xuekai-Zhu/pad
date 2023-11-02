def solution():
    """Donny has $78 in his piggy bank. If Donny buys a kite for $8 and a frisbee for $9. How much money does Donny have left?"""
    # Define the initial amount of money Donny has
    initial_amount = 78

    # Define the cost of the kite and frisbee
    kite_cost = 8
    frisbee_cost = 9

    # Calculate the total cost of the purchases
    total_cost = kite_cost + frisbee_cost

    # Calculate the amount of money Donny has left
    remaining_amount = initial_amount - total_cost

    # Display the remaining amount of money
    result = remaining_amount
    return result

print(solution())