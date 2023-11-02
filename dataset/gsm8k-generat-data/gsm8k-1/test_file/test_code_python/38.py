def solution():
    """Grandma Jones baked 5 apple pies for the fireman's luncheon. She cut each pie into 8 pieces and set the five pies out on the buffet table for the guests to serve themselves. At the end of the evening, after the guests had taken and eaten their pieces of pie, there were 14 pieces of pie remaining. How many pieces were taken by the guests?"""
    pies_baked = 5
    pieces_per_pie = 8
    pieces_leftover = 14
    pieces_taken = (pies_baked * pieces_per_pie) - pieces_leftover
    result = pieces_taken
    return result

print(solution())