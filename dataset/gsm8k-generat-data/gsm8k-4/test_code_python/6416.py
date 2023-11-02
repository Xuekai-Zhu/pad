def solution():
    """Frank is practicing a new dance move. It starts with him take 5 steps back, and then 10 steps forward, and then 2 steps back, and then double that amount forward. How many steps forward is Frank from his original starting point?"""
    # Define the number of steps taken by Frank
    steps_back = 5
    steps_forward_1 = 10
    steps_back_2 = 2
    steps_forward_2 = steps_back_2 * 2
    
    # Calculate the net number of steps taken by Frank
    net_steps = steps_forward_1 + steps_forward_2 - steps_back - steps_back_2

    result = net_steps
    return result

print(solution())