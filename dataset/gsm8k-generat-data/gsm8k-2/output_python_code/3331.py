def solution():
    """Nancy and Jason are learning to dance for the first time. Nancy steps on her partner's feet 3 times as often as Jason. If together they step on each other's feet 32 times, how many times does Jason step on his partner's feet?"""
    total_steps = 32
    nancy_steps = 3
    jason_steps = 1
    jason_total_steps = total_steps / (nancy_steps + jason_steps)
    result = jason_total_steps
    return result

print(solution())