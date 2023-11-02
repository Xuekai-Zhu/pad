def solution():
    # Calculate the total number of tissues Tucker bought and used
    total_tissues = 160 * 3  # each box contains 160 tissues and Tucker bought 3 boxes
    used_tissues = 210  # number of tissues used while sick with the flu

    # Calculate the number of tissues Tucker would have left
    tissues_left = total_tissues - used_tissues
    result = tissues_left
    return result

print(solution())