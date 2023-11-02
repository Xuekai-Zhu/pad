def solution():
    """A supermarket receives a delivery of 15 cases of tins of beans. Each case contains 24 tins. If 5% of the tins are damaged and thrown away, how many tins of beans are left?"""
    # Define the number of cases and tins per case
    NUM_CASES = 15
    TINS_PER_CASE = 24

    # Calculate the total number of tins
    total_tins = NUM_CASES * TINS_PER_CASE

    # Calculate the number of tins that are damaged
    damaged_tins = total_tins * 0.05

    # Calculate the number of tins that are left
    remaining_tins = total_tins - damaged_tins

    # return the result
    result = remaining_tins
    return result

print(solution())