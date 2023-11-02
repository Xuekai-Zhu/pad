def solution():
    num_rows = 50
    flowers_per_row = 400
    cut_percentage = 0.6  # 60% cut

    # Calculate the total number of flowers in the garden
    total_flowers = num_rows * flowers_per_row

    # Calculate the number of flowers cut
    cut_flowers = total_flowers * cut_percentage

    # Calculate the number of flowers remaining
    remaining_flowers = total_flowers - cut_flowers
    result = remaining_flowers
    return result

print(solution())