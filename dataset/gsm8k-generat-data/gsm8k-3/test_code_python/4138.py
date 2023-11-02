def solution():
    """Agatha has some money to spend on a new bike. She spends $15 on the frame, and $25 on the front wheel. If she has $20 left to spend on a seat and handlebar tape, how much money, in dollars, did she have at first?"""
    # Define the cost of the frame and front wheel
    FRAME_COST = 15
    WHEEL_COST = 25

    # Define the remaining amount for the seat and handlebar tape
    REMAINING_AMOUNT = 20

    # Calculate the total cost of the frame and front wheel
    total_cost = FRAME_COST + WHEEL_COST

    # Calculate the amount Agatha had at first
    amount_at_first = total_cost + REMAINING_AMOUNT

    # Display the amount Agatha had at first
    result = amount_at_first
    return result

print(solution())