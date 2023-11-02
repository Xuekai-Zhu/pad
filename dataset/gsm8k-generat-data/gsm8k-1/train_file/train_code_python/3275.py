def solution():
    """If you take the fastest speed of a rabbit and double it, add 4 to that then double it again you get 188. How fast is the rabbit?"""
    final_speed = 188
    # reverse operations to find initial speed
    doubled_speed_minus_four = final_speed / 2
    initial_speed = (doubled_speed_minus_four - 4) / 2
    result = initial_speed
    return result

print(solution())