def solution():
    # Define the number of total chickens and the ratio of hens to roosters
    total_chickens = 75
    hens_to_roosters_ratio = 9 - 5

    # Calculate the total number of hens
    total_hens = (hens_to_roosters_ratio / 10) * total_chickens

    result = total_hens
    return result

print(solution())