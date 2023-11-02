def solution():
    """Frank is practicing a new dance move. It starts with him take 5 steps back, and then 10 steps forward, and then 2 steps back, and then double that amount forward. How many steps forward is Frank from his original starting point?"""
    starting_point = 0
    back_steps = 5 + 2
    forward_steps = 10 + (2 * 2)
    total_steps = forward_steps - back_steps
    result = total_steps
    return result

print(solution())