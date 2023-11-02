def solution():
    # Calculate the total number of petals in Mabel's garden
    total_petals = 5 * 8

    # Calculate the number of petals on the two daisies she gave to her teacher
    petals_given = 2 * 8

    # Calculate the number of petals on the remaining daisies in her garden
    remaining_petals = total_petals - petals_given

    result = remaining_petals
    return result

print(solution())