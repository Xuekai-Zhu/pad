def solution():
    """A box of six popsicles was left out in the sun and is slowly melting. Every time a popsicle melts the remaining popsicles melt twice as fast as the previous one. How many times faster than the first popsicle does the last popsicle’s remains melt?"""
    # Define the initial melting rate of the popsicles
    initial_rate = 1

    # Define the number of popsicles
    num_popsicles = 6

    # Define the total melting rate of the popsicles
    total_rate = 0

    # Calculate the total melting rate of the popsicles
    for i in range(num_popsicles):
        rate = initial_rate * 2 ** i
        total_rate += rate

    # Calculate the ratio of the melting rate of the last popsicle to the initial rate
    ratio = total_rate / initial_rate

    # Return the result
    result = round(ratio, 1)
    return result

print(solution())