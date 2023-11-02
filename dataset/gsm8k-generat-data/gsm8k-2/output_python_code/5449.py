def solution():
    """A group of hawks is called a kettle. It is breeding season for hawks. A group of ornithologists are tracking 6 kettles of hawks. Each kettle has an average of 15 pregnancies that yield 4 babies per batch. How many babies are expected this season if approximately 25% are lost?"""
    total_pregnancies = 6 * 15
    total_babies = total_pregnancies * 4
    lost_babies = total_babies * 0.25
    expected_babies = total_babies - lost_babies
    result = expected_babies
    return result

print(solution())