def solution():
    """A dog is being treated for fleas. One flea treatment gets rid of half the fleas. After four treatments, the dog has 14 fleas left. How many more fleas did the dog have before the flea treatments than after?"""
    # Initialize variables
    fleas_before = 0
    fleas_after = 14

    # Calculate the number of fleas before the treatments
    for i in range(4):
        fleas_after *= 2
    fleas_before = fleas_after

    # Calculate the difference in the number of fleas
    difference = fleas_before - fleas_after

    # Display the difference
    result = difference
    return result

print(solution())