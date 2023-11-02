def solution():
    
    current_swans = 15
    doubling_period = 2
    years = 10
    num_doublings = years / doubling_period
    swans = current_swans * (2 ** num_doublings)
    result = swans
    return result

print(solution())