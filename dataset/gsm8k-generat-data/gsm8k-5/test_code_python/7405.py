def solution():
    total_budget = 60  # Agatha has $60 to spend
    frame_cost = 15  # Agatha spends $15 on the frame
    wheel_cost = 25  # Agatha spends $25 on the front wheel

    # Calculate the amount Agatha has left to spend
    remaining_budget = total_budget - frame_cost - wheel_cost
    result = remaining_budget
    return result

print(solution())