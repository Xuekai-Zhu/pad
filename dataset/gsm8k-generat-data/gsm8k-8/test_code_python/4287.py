def solution():
    # Define the number of plates decorated with a whole sprig of parsley
    whole_plates = 8

    # Define the number of plates decorated with 1/2 a sprig of parsley
    half_plates = 12

    # Calculate the total sprigs of parsley used
    total_parsley_used = whole_plates + half_plates / 2

    # Calculate the sprigs of parsley left
    parsley_left = 25 - total_parsley_used
    result = parsley_left
    return result

print(solution())