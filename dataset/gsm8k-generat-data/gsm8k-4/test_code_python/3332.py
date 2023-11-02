def solution():
    """Nancy and Jason are learning to dance for the first time. Nancy steps on her partner's feet 3 times as often as Jason. If together they step on each other's feet 32 times, how many times does Jason step on his partner's feet?"""
    # Let's assume Jason steps on his partner's feet x times
    jason_steps = x

    # Then, Nancy steps on her partner's feet 3 times as often as Jason
    nancy_steps = 3 * x

    # Together they step on each other's feet 32 times
    total_steps = jason_steps + nancy_steps
    
    # We can set up the equation: jason_steps + 3 * jason_steps = 32
    # Which simplifies to 4 * jason_steps = 32
    # Then solve for jason_steps
    jason_steps = 8
    
    # Therefore, Jason steps on his partner's feet 8 times
    result = jason_steps
    return result

print(solution())