def solution():
    """There are 4 alligators living on a golf course in Florida. If the number of alligators doubles every six months, how many alligators will there be at the end of a year?"""
    starting_alligators = 4
    doubling_periods = 2  # there are two 6 month periods in a year
    total_alligators = starting_alligators * (2 ** doubling_periods)
    result = total_alligators
    return result

print(solution())