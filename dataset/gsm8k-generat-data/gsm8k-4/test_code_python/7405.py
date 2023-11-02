def solution():
    """Agatha has $60 to spend on a new bike. She spends $15 on the frame, and $25 on the front wheel. What does she have left, in dollars, to spend on a seat and handlebar tape?"""
    # Define the amount spent on the frame and front wheel
    frame_cost = 15
    wheel_cost = 25

    # Define the total budget
    total_budget = 60

    # Calculate the amount spent so far
    amount_spent = frame_cost + wheel_cost

    # Calculate the amount remaining to spend on a seat and handlebar tape
    remaining_amount = total_budget - amount_spent

    # Return the result
    result = remaining_amount
    return result

print(solution())