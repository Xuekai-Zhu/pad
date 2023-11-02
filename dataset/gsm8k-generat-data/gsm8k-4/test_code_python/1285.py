def solution():
    """There are twice as many surfers on Malibu beach as in Santa Monica beach. If there are 20 surfers in Santa Monica, calculate the total number of surfers on the two beaches."""
    # Define the number of surfers in Santa Monica and calculate the number in Malibu
    santa_monica_surfers = 20
    malibu_surfers = santa_monica_surfers * 2

    # Calculate the total number of surfers on the two beaches
    total_surfers = santa_monica_surfers + malibu_surfers

    # Return the result
    result = total_surfers
    return result

print(solution())