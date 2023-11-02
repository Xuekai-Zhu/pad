def solution():
    # Calculate the total length that needs to be covered with bushes
    total_length = 16 * 3  # each side is 16 feet long and there are 3 sides

    # Calculate the number of bushes needed to cover the length
    num_bushes = total_length // 4  # each bush fills 4 feet

    result = num_bushes
    return result

print(solution())