def solution():
    # Calculate the total length of fishing line John has
    total_length = 3 * 100  # John buys 3 reels of 100m fishing line

    # Calculate the number of 10m sections John can cut from the fishing line
    num_sections = total_length // 10  # John cuts the fishing line into 10m sections

    result = num_sections
    return result

print(solution())