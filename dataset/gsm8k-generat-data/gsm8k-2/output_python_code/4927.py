def solution():
    """Every 2 years, the number of swans at Rita's pond doubles. Currently, there are 15 swans in the pond. How many swans will there be in ten years?"""
    current_swans = 15
    doubling_time_years = 2
    years = 10
    doubling_times = years // doubling_time_years
    total_swans = current_swans * (2 ** doubling_times)
    result = total_swans
    return result

print(solution())