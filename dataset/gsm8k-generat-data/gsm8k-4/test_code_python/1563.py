def solution():
    """Aaron has four times as many cows as Matthews. Together, they have 30 more cows than Marovich. If Matthews has 60 cows, how many cows do the three have altogether?"""
    # Define the number of cows Matthews has
    matthews_cows = 60

    # Calculate the number of cows Aaron has
    aaron_cows = matthews_cows * 4

    # Calculate the total number of cows owned by Aaron and Matthews
    total_cows = matthews_cows + aaron_cows

    # Calculate the number of cows Marovich has
    marovich_cows = total_cows - 30

    # Calculate the total number of cows owned by all three
    all_cows = matthews_cows + aaron_cows + marovich_cows

    result = all_cows
    return result

print(solution())