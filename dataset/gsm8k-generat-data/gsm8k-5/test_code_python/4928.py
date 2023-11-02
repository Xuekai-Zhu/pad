def solution():
    initial_swans = 15  # There are currently 15 swans in the pond
    doubling_period = 2  # The number of swans doubles every 2 years
    years = 10  # We want to know how many swans there will be in 10 years

    # Calculate the number of doublings that will occur in 10 years
    num_doublings = years / doubling_period

    # Calculate the final number of swans after the doublings
    final_swans = initial_swans * (2 ** num_doublings)
    result = final_swans
    return result

print(solution())