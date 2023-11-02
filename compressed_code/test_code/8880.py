def solution():
    
    starting_alligators = 4
    doubling_periods = 2  
    total_alligators = starting_alligators * (2 ** doubling_periods)
    result = total_alligators
    return result

print(solution())