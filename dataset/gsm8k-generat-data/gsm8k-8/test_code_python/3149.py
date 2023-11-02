def solution():
    # Define the length of Isaac's ribbon
    length_of_ribbon = 30

    # Divide the ribbon into 6 equal parts
    each_part_length = length_of_ribbon / 6

    # Determine how much ribbon is used
    used_ribbon = 4 * each_part_length

    # Calculate how much ribbon is left
    remaining_ribbon = length_of_ribbon - used_ribbon
    result = remaining_ribbon
    return result

print(solution())