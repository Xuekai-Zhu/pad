def solution():
    """Jim is making a comforter for his king-sized bed. He needs two pieces of fabric that are 2 feet longer and 2 feet wider than the bed, which measures 6 feet long by 8 feet wide. How many square feet of fabric does Jim need to buy?"""
    bed_length = 6
    bed_width = 8
    fabric_length = bed_length + 2
    fabric_width = bed_width + 2
    fabric_area = fabric_length * fabric_width * 2
    result = fabric_area
    return result

print(solution())