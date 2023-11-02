def solution():
    """A group of hawks is called a kettle. It is breeding season for hawks. A group of ornithologists are tracking 6 kettles of hawks. Each kettle has an average of 15 pregnancies that yield 4 babies per batch. How many babies are expected this season if approximately 25% are lost?"""
    # Define the number of kettles and pregnancies per kettle
    num_kettles = 6
    num_pregnancies = 15

    # Calculate the total number of babies expected
    num_babies = num_kettles * num_pregnancies * 4

    # Calculate the number of lost babies
    lost_babies = num_babies * 0.25

    # Calculate the net number of babies expected
    net_babies = num_babies - lost_babies

    # return the result
    result = net_babies
    return result

print(solution())