def solution():
    """Agatha has $60 to spend on a new bike. She spends $15 on the frame, and $25 on the front wheel. What does she have left, in dollars, to spend on a seat and handlebar tape?"""
    total_budget = 60
    frame_cost = 15
    wheel_cost = 25
    remaining_budget = total_budget - frame_cost - wheel_cost
    result = remaining_budget
    return result

print(solution())