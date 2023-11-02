def solution():
    """John buys 3 reels of 100m fishing line. He cuts it into 10m sections. How many sections does he get?"""
    reel_length = 100
    num_reels = 3
    section_length = 10
    total_sections = (reel_length * num_reels) / section_length
    result = total_sections
    return result

print(solution())