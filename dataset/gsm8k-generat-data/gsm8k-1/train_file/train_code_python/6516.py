def solution():
    """Mabel lives 4500 steps directly east of Lake High school. Helen lives 3/4 the number of steps that Mabel lives, directly west of the school. What's the total number of steps Mabel will walk to visit Helen so that they can do their assignments together?"""
    mabel_steps = 4500
    helen_steps = (3/4)*mabel_steps
    total_steps = mabel_steps + helen_steps
    result = total_steps
    return result

print(solution())