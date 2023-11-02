def solution():
    num_frames = 3
    frame_cost = 3
    money_paid = 20

    # Calculate the total cost of all frames
    total_cost = num_frames * frame_cost

    # Calculate the amount of change Sally will receive
    change = money_paid - total_cost
    result = change
    return result

print(solution())