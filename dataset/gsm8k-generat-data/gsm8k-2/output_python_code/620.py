def solution():
    """There are 36 seagulls on the roof of the Taco Bell. Kids scare 1/4 of them away by throwing stones, and 1/3 of the remaining birds decide to fly to McDonald's parking lot. How many seagulls are left?"""
    initial_seagulls = 36
    scared_seagulls = initial_seagulls * 0.25
    remaining_seagulls = initial_seagulls - scared_seagulls
    flying_seagulls = remaining_seagulls * (1/3)
    final_seagulls = remaining_seagulls - flying_seagulls
    result = final_seagulls
    return result

print(solution())