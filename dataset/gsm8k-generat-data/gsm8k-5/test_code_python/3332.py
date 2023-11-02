def solution():
    total_steps = 32  # Together, Nancy and Jason step on each other's feet 32 times
    nancy_steps = 3/4 * total_steps  # Nancy steps on her partner's feet 3 times as often as Jason
    jason_steps = total_steps - nancy_steps  # Calculate how many times Jason steps on his partner's feet

    result = jason_steps
    return result

print(solution())