def solution():
    """Aaron has four times as many cows as does Matthews. Together, they have 30 more cows than Marovich. If Matthews has 60 cows, how many cows do the three have altogether?"""
    # Define the number of cows owned by Matthews
    matthews_cows = 60

    # Calculate the number of cows owned by Aaron
    aaron_cows = matthews_cows * 4

    # Calculate the number of cows owned by Marovich
    marovich_cows = aaron_cows + matthews_cows - 30

    # Calculate the total number of cows
    total_cows = aaron_cows + matthews_cows + marovich_cows

    # Display the total number of cows
    result = total_cows
    return result

print(solution())