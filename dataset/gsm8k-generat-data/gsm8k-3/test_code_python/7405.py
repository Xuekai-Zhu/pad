def solution():
    """Agatha has $60 to spend on a new bike. She spends $15 on the frame, and $25 on the front wheel. What does she have left, in dollars, to spend on a seat and handlebar tape?"""
    # Define the initial budget and the cost of the frame and front wheel
    budget = 60
    frame_cost = 15
    wheel_cost = 25

    # Calculate the remaining budget after purchasing the frame and front wheel
    remaining_budget = budget - frame_cost - wheel_cost

    # Display the remaining budget
    result = remaining_budget
    return result

print(solution())