def solution():
    cost_per_frame = 3  # Each frame costs $3
    num_frames = 3  # Sally bought 3 frames
    total_cost = cost_per_frame * num_frames  # Calculate the total cost of the frames
    paid_with = 20  # Sally paid with a $20 bill

    # Calculate the amount of change Sally received
    change = paid_with - total_cost
    result = change
    return result

print(solution())