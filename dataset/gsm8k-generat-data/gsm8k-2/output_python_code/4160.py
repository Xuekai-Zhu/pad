def solution():
    """Mr. Wells has a garden of flowers with 50 rows. If each row has 400 flowers and Mr. Wells cuts 60% of the flowers, how many flowers are remaining in the garden?"""
    total_flowers = 50 * 400
    cut_flowers = total_flowers * 0.6
    remaining_flowers = total_flowers - cut_flowers
    result = remaining_flowers
    return result

print(solution())