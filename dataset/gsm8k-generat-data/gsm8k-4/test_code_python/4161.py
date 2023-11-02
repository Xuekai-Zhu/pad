def solution():
    """Mr. Wells has a garden of flowers with 50 rows. If each row has 400 flowers and Mr. Wells cuts 60% of the flowers, how many flowers are remaining in the garden?"""
    # Define the number of rows and flowers per row
    rows = 50
    flowers_per_row = 400

    # Calculate the total number of flowers in the garden
    total_flowers = rows * flowers_per_row

    # Calculate the number of flowers cut
    cut_flowers = total_flowers * 0.6

    # Calculate the number of remaining flowers
    remaining_flowers = total_flowers - cut_flowers

    result = remaining_flowers
    return result

print(solution())