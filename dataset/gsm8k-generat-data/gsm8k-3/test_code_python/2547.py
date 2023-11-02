def solution():
    """John buys 3 reels of 100m fishing line. He cuts it into 10m sections. How many sections does he get?"""
    # Define the length of each reel in meters
    reel_length = 100

    # Define the length of each section in meters
    section_length = 10

    # Calculate the total number of sections
    total_sections = 3 * (reel_length // section_length)

    # Display the total number of sections
    result = total_sections
    return result

print(solution())