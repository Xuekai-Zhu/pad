def solution():
    # Define the height differences between the poodles
    standard_to_miniature_diff = 8
    miniature_to_toy_diff = 6

    # Calculate the height difference between the standard and toy poodle
    standard_to_toy_diff = standard_to_miniature_diff + miniature_to_toy_diff

    # Calculate the height of the toy poodle
    toy_height = 28 - standard_to_toy_diff
    result = toy_height
    return result

print(solution())