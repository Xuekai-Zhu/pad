def solution():
    """A supermarket receives a delivery of 15 cases of tins of beans. Each case contains 24 tins. If 5% of the tins are damaged and thrown away, how many tins of beans are left?"""
    # Define the number of cases and tins per case
    cases = 15
    tins_per_case = 24

    # Calculate the total number of tins
    total_tins = cases * tins_per_case

    # Calculate the number of damaged tins
    damaged_tins = int(0.05 * total_tins)

    # Calculate the number of tins left after removing damaged tins
    tins_left = total_tins - damaged_tins

    # Display the number of tins left
    result = tins_left
    return result

print(solution())