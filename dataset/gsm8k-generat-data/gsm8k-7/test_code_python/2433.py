def solution():
    initial_length = 100

    # Cut the rope in half
    half_length = initial_length / 2

    # Cut one of the halves in half again
    quarter_length = half_length / 2

    # Cut one of the remaining quarters into fifths
    fifth_length = quarter_length / 5

    # Determine the length of the rope Josh is holding
    final_length = fifth_length
    result = final_length
    return result

print(solution())