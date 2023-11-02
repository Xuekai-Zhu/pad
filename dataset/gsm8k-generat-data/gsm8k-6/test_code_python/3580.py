def solution():
    # Calculate the number of seedlings planted by Remi on the second day
    seedlings_second_day = 2 * 200

    # Calculate the total number of seedlings planted by Remi and his father
    total_seedlings = 200 + seedlings_second_day

    # Calculate the number of seedlings planted by Remi's father
    father_seedlings = 1200 - total_seedlings

    result = father_seedlings
    return result

print(solution())