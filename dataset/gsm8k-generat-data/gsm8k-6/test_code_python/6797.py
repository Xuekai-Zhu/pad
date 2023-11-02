def solution():
    # Calculate the number of sit-ups performed by Barney, Carrie, and Jerrie
    sit_ups_B = 45
    sit_ups_C = 2 * sit_ups_B
    sit_ups_J = (sit_ups_C + 5) * 3

    # Calculate the combined total number of sit-ups performed
    total_sit_ups = sit_ups_B + sit_ups_C * 2 + sit_ups_J * 3
    result = total_sit_ups
    return result

print(solution())