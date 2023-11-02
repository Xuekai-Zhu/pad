def solution():
    """In the beginning, Justine had 10 more rubber bands than Bailey but 2 fewer bands than Ylona. Bailey decided to give two bands each to Justine and Ylona so that he is left with only 8 rubber bands. How many rubber bands did Ylona have in the beginning?"""
    bailey_bands = 8
    justine_bands = bailey_bands + 2
    ylona_bands = justine_bands + 2
    total_bands = bailey_bands + justine_bands + ylona_bands
    initial_yola_bands = total_bands - justine_bands + 10 - 2
    result = initial_yola_bands
    return result

print(solution())