def solution():
    """Frank is practicing a new dance move. It starts with him take 5 steps back, and then 10 steps forward, and then 2 steps back, and then double that amount forward. How many steps forward is Frank from his original starting point?"""
    steps_back_1 = 5
    steps_forward_1 = 10
    steps_back_2 = 2
    steps_forward_2 = 2 * steps_back_2
    total_steps = -steps_back_1 + steps_forward_1 - steps_back_2 + steps_forward_2
    result = total_steps
    return result

print(solution())