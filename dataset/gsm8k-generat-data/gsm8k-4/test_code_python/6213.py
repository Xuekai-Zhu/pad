def solution():
    """Sally bought 3 photograph frames, each costing her $3. She paid with a $20 bill. How much change did she get?"""
    # Define the cost of each photograph frame and the number of frames purchased
    FRAME_COST = 3
    NUM_FRAMES = 3

    # Calculate the total cost of the frames
    total_cost = FRAME_COST * NUM_FRAMES

    # Calculate the amount of change she will receive
    change = 20 - total_cost

    # return the result
    result = change
    return result

print(solution())