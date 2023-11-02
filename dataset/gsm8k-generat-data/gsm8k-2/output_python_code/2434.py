def solution():
    """In 5 years, Frank will be three times as old as Ty is now. Ty is currently 4 years more than two times as old as Carla is now. Carla is currently 2 years older than Karen is now. If Karen is currently 2 years old, how old will Frank be in 5 years?"""
    karen_age = 2
    carla_age = karen_age + 2
    ty_age = 2 * carla_age + 4
    frank_age = 3 * (ty_age + 5) - 5
    result = frank_age + 5
    return result

print(solution())