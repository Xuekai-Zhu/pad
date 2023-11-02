def solution():
    """John buys 3 reels of 100m fishing line. He cuts it into 10m sections. How many sections does he get?"""
    length_of_fishing_line = 300
    section_length = 10
    sections = length_of_fishing_line // section_length
    result = sections
    return result

print(solution())