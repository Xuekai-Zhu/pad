def solution():
    """Nancy and Jason are learning to dance for the first time. Nancy steps on her partner's feet 3 times as often as Jason. If together they step on each other's feet 32 times, how many times does Jason step on his partner's feet?"""
    total_steps = 32
    jason_steps = total_steps / 4
    nancy_steps = jason_steps * 3
    result = jason_steps
    return result

print(solution())