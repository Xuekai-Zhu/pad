def solution():
    frame_cost = 15  # Cost of the bike frame is $15
    front_wheel_cost = 25  # Cost of the front wheel is $25
    remaining_budget = 20  # Agatha has $20 left to spend on a seat and handlebar tape

    # Calculate the total cost of the bike
    total_cost = frame_cost + front_wheel_cost + remaining_budget

    # Calculate the initial amount of money Agatha had
    initial_budget = total_cost - remaining_budget
    result = initial_budget
    return result

print(solution())