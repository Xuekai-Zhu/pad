def solution():
    # Define the sizes of the countries as ratios to the United States
    canada_ratio = 1.5
    russia_ratio = 1.33 * canada_ratio

    # Calculate the ratio of Russia's size to the United States' size
    russia_to_us = russia_ratio / canada_ratio

    result = russia_to_us
    return result

print(solution())