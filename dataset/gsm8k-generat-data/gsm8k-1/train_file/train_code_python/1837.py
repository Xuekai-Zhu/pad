def solution():
    """Jacob loves to build things. In Jacob's toy bin there are 18 red blocks. There are 7 more yellow blocks than red blocks. There are also 14 more blue blocks than red blocks. How many blocks are there in all?"""
    red_blocks = 18
    yellow_blocks = red_blocks + 7
    blue_blocks = red_blocks + 14
    total_blocks = red_blocks + yellow_blocks + blue_blocks
    result = total_blocks
    return result

print(solution())