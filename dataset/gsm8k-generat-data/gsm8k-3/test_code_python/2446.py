def solution():
    """Bob and Jim decide to skip rocks.  Bob can skip a rock 12 times.  Jim can skip a rock 15 times.  If they each skipped 10 rocks how many total skips did they get?"""
    # Define the number of rocks skipped and the number of skips per person
    rocks_skipped = 10
    bob_skips = 12
    jim_skips = 15

    # Calculate the total number of skips
    total_skips = (bob_skips + jim_skips) * rocks_skipped

    # Display the total number of skips
    result = total_skips
    return result

print(solution())