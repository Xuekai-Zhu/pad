def solution():
    total_flowers = 25 + 40 + 35  # There are 25 roses, 40 tulips, and 35 daisies
    non_roses = total_flowers - 25  # Subtract the number of roses to get the number of non-roses
    percentage_non_roses = (non_roses / total_flowers) * 100  # Calculate the percentage of non-roses

    result = percentage_non_roses
    return result

print(solution())