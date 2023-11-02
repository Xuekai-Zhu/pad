def solution():
    # Define the number of shirts
    num_shirts = 4

    # Calculate the number of pants (twice the number of shirts)
    num_pants = 2 * num_shirts

    # Calculate the number of shorts (half the number of pants)
    num_shorts = 0.5 * num_pants

    # Calculate the total number of pieces of clothing donated
    total_clothes = num_shirts + num_pants + num_shorts
    result = total_clothes
    return result

print(solution())