def solution():
    """Carl has a cane that is half as long as he is tall. Carl is one foot taller than his brother, Ned. And Ned is two feet shorter than his cousin, Isabel. If Isabel is 7 feet tall, how long is Carl's cane, in feet?"""
    isabel_height = 7
    ned_height = isabel_height - 2
    carl_height = ned_height + 1
    cane_length = carl_height * 0.5
    result = cane_length
    return result

print(solution())