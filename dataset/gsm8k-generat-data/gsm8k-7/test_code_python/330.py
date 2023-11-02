def solution():
    num_expected = 220
    percent_not_showing = 0.05

    # Calculate the number of people who are expected to show up
    num_showing_up = num_expected * (1 - percent_not_showing)

    result = num_showing_up
    return result

print(solution())