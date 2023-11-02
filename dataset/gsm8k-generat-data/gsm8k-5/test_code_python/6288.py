def solution():
    initial_plates = 27  # Alice starts with 27 plates
    added_plates = 37  # Alice adds 37 more plates
    total_plates = 83  # The tower crashes down with 83 plates

    # Calculate the number of plates Alice was able to add before the tower fell
    remaining_plates = total_plates - initial_plates - added_plates
    result = remaining_plates
    return result

print(solution())