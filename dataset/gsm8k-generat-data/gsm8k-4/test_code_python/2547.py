def solution():
    """John buys 3 reels of 100m fishing line. He cuts it into 10m sections. How many sections does he get?"""
    # Define the length of each reel and the length of each section
    REEL_LENGTH = 100
    SECTION_LENGTH = 10

    # Calculate the total length of the fishing line
    total_length = REEL_LENGTH * 3

    # Calculate the number of sections that can be cut from the total length
    num_sections = total_length // SECTION_LENGTH

    # return the result
    result = num_sections
    return result

print(solution())