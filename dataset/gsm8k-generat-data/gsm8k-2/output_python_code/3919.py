def solution():
    """There are 4 alligators living on a golf course in Florida. If the number of alligators doubles every six months, how many alligators will there be at the end of a year?"""
    initial_alligators = 4
    doubling_periods = 2
    final_alligators = initial_alligators * (2 ** doubling_periods)
    result = final_alligators
    return result

print(solution())