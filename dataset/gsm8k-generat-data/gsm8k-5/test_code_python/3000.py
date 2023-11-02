def solution():
    original_length = 20  # The original length of the pole is 20 meters
    percentage_cut = 30  # The pole was cut by 30%

    # Calculate the length of the pole after the cut
    cut_length = original_length - (original_length * (percentage_cut/100))

    result = cut_length
    return result

print(solution())