def solution():
    # Calculate the total number of flowers in the garden
    total_flowers = 50 * 400

    # Calculate the number of flowers Mr. Wells cuts
    cut_flowers = 0.6 * total_flowers

    # Calculate the number of flowers remaining in the garden
    remaining_flowers = total_flowers - cut_flowers
    result = remaining_flowers
    return result

print(solution())