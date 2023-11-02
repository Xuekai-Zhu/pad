def solution():
    """A box of six popsicles was left out in the sun and is slowly melting. Every time a popsicle melts the remaining popsicles melt twice as fast as the previous one. How many times faster than the first popsicle does the last popsicle’s remains melt?"""
    # Define the initial melting rate of each popsicle
    initial_rate = 1

    # Calculate the total melting rate of all the popsicles
    total_rate = 0
    for i in range(6):
        total_rate += initial_rate * (2 ** i)

    # Calculate the melting rate of the last popsicle
    last_rate = initial_rate * (2 ** 5)

    # Calculate how many times faster the last popsicle melts compared to the first one
    ratio = last_rate / initial_rate

    # Display the ratio
    result = ratio
    return result

print(solution())