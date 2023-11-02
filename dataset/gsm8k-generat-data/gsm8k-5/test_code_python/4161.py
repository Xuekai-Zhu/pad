def solution():
    total_flowers = 50 * 400  # Total number of flowers in the garden
    cut_flowers = 0.6 * total_flowers  # Number of flowers to be cut

    # Calculate the number of remaining flowers
    remaining_flowers = total_flowers - cut_flowers
    result = remaining_flowers
    return result

print(solution())