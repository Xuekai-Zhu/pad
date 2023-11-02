def solution():
    """Every 2 years, the number of swans at Rita's pond doubles. Currently, there are 15 swans in the pond. How many swans will there be in ten years?"""
    current_swans = 15
    doubling_period = 2
    years = 10
    num_doublings = years / doubling_period
    swans = current_swans * (2 ** num_doublings)
    result = swans
    return result

print(solution())