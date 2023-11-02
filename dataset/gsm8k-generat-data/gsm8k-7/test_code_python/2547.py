def solution():
    num_reels = 3
    reel_length = 100
    section_length = 10

    # Calculate the total length of fishing line
    total_length = num_reels * reel_length

    # Calculate the number of sections
    num_sections = total_length / section_length
    result = num_sections
    return result

print(solution())