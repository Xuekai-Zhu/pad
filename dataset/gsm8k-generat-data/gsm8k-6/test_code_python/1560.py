def solution():
    # Calculate the cost of the frame Yvette initially intended to buy
    initial_frame_cost = 60 / 1.2  # the frame is 20% more expensive than her budget of $60

    # Calculate the cost of the smaller frame she bought
    smaller_frame_cost = initial_frame_cost * 0.75  # the smaller frame is 3/4 the new price of the initial frame

    # Calculate how much money Yvette remained with
    money_left = 60 - smaller_frame_cost
    result = money_left
    return result

print(solution())