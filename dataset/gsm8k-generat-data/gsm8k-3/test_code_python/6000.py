def solution():
    """If it takes 8 days for 3 builders to build a cottage. How long will it take 6 builders to build the same size cottage working at the same rate?"""
    # Define the number of builders and the time it takes to build the cottage
    builders1 = 3
    time1 = 8

    # Calculate the rate of building
    rate1 = 1 / (builders1 * time1)

    # Define the new number of builders
    builders2 = 6

    # Calculate the new time it takes to build the cottage
    time2 = 1 / (builders2 * rate1)

    # Display the new time
    result = time2
    return result

print(solution())