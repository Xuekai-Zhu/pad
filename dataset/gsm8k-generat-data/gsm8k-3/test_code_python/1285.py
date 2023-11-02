def solution():
    """There are twice as many surfers on Malibu beach as in Santa Monica beach. If there are 20 surfers in Santa Monica, calculate the total number of surfers on the two beaches."""
    # Define the number of surfers in Santa Monica
    santa_monica_surfers = 20

    # Calculate the number of surfers in Malibu
    malibu_surfers = 2 * santa_monica_surfers

    # Calculate the total number of surfers on the two beaches
    total_surfers = santa_monica_surfers + malibu_surfers

    # Display the total number of surfers
    result = total_surfers
    return result

print(solution())