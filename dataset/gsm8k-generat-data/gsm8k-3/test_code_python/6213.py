def solution():
    """Sally bought 3 photograph frames, each costing her $3. She paid with a $20 bill. How much change did she get?"""
    # Define the cost of each photograph frame
    frame_cost = 3

    # Define the number of photograph frames purchased
    num_frames = 3

    # Calculate the total cost of the photograph frames
    total_cost = frame_cost * num_frames

    # Calculate the amount of change Sally will receive
    change = 20 - total_cost

    # Display the amount of change
    result = change
    return result

print(solution())