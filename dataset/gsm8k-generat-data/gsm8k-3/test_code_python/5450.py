def solution():
    """A group of hawks is called a kettle. It is breeding season for hawks. A group of ornithologists are tracking 6 kettles of hawks. Each kettle has an average of 15 pregnancies that yield 4 babies per batch.  How many babies are expected this season if approximately 25% are lost?"""
    # Define the number of kettles and pregnancies per kettle
    kettles = 6
    pregnancies = 15

    # Define the number of babies per batch and the loss rate
    babies_per_batch = 4
    loss_rate = 0.25

    # Calculate the total number of babies expected
    total_babies = kettles * pregnancies * babies_per_batch
    expected_babies = total_babies * (1 - loss_rate)

    # Display the number of babies expected
    result = expected_babies
    return result

print(solution())