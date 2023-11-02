def solution():
    initial_group_size = 4  # Erika has 3 siblings
    additional_friends = 3
    initial_chalk_count = (initial_group_size + additional_friends) * 3  # Each person originally had 3 pieces of chalk

    # Accounting for the lost chalk and the additional 12 pieces, calculate the new total count
    new_chalk_count = initial_chalk_count - 2 + 12

    # Calculate the original chalk count by subtracting the additional chalk from the new count
    original_chalk_count = new_chalk_count - 3 * (initial_group_size + additional_friends)

    result = original_chalk_count
    return result

print(solution())