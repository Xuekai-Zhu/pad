def solution():
    """Mabel has 5 daisies in her garden, and each daisy has 8 petals. If she gives 2 daisies to her teacher, how many petals does she have on the remaining daisies in her garden?"""
    # Define the number of daisies and petals per daisy
    daisies = 5
    petals_per_daisy = 8

    # Calculate the total number of petals before giving daisies to the teacher
    total_petals_before = daisies * petals_per_daisy

    # Calculate the number of daisies and petals after giving 2 daisies to the teacher
    daisies_after = daisies - 2
    petals_per_daisy_after = petals_per_daisy

    # Calculate the total number of petals after giving daisies to the teacher
    total_petals_after = daisies_after * petals_per_daisy_after

    result = total_petals_after
    return result

print(solution())