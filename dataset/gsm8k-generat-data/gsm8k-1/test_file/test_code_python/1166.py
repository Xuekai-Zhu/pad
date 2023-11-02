def solution():
    """A wall mural has four different colors of paint in it: red, white, purple, and yellow. There are equal amounts of red, white, and purple paint in the mural. Half the mural is yellow. If the mural used 12 pints of paint in all, how many pints of red paint was used?"""
    total_paint = 12
    yellow_paint = total_paint / 2
    red_paint = (total_paint - yellow_paint) / 3
    result = red_paint
    return result

print(solution())