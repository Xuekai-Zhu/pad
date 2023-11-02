def solution():
    """A dog is being treated for fleas. One flea treatment gets rid of half the fleas. After four treatments, the dog has 14 fleas left. How many more fleas did the dog have before the flea treatments than after?"""
    num_fleas_after = 14
    num_fleas_before = num_fleas_after
    for i in range(4):
        num_fleas_before *= 2
    result = num_fleas_before - num_fleas_after
    return result

print(solution())