def solution():
    
    initial_alligators = 4
    doubling_periods = 2
    final_alligators = initial_alligators * (2 ** doubling_periods)
    result = final_alligators
    return result

print(solution())