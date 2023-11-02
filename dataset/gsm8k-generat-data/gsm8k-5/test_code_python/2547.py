def solution():
    total_length = 3 * 100  # John buys 3 reels of 100m fishing line
    section_length = 10  # John cuts the line into 10m sections

    # Calculate the total number of sections
    total_sections = total_length / section_length
    result = total_sections
    return result

print(solution())