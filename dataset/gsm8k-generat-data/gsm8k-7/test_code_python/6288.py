def solution():
    starting_plates = 27
    added_plates = 37
    total_plates = 83

    # Calculate the number of plates Alice was able to add before the tower fell
    num_added_plates = total_plates - starting_plates - added_plates
    result = num_added_plates
    return result

print(solution())