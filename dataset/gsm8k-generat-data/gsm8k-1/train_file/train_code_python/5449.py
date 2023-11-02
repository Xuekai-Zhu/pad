def solution():
    """A group of hawks is called a kettle. It is breeding season for hawks. A group of ornithologists are tracking 6 kettles of hawks. Each kettle has an average of 15 pregnancies that yield 4 babies per batch. How many babies are expected this season if approximately 25% are lost?"""
    num_kettles = 6
    num_pregnancies = 15
    num_babies_per_pregnancy = 4
    total_babies = num_kettles * num_pregnancies * num_babies_per_pregnancy
    lost_babies = 0.25 * total_babies
    expected_babies = total_babies - lost_babies
    result = expected_babies
    return result

print(solution())