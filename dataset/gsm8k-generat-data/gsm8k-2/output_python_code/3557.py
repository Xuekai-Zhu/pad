def solution():
    """Rocky boxed 190 fights in his career. 50 percent of his fights were knockouts, and 20 percent of the knockouts were in the first round. How many knockouts did Rocky have in the first round?"""
    total_fights = 190
    knockout_percentage = 0.5
    first_round_percentage = 0.2
    total_knockouts = total_fights * knockout_percentage
    first_round_knockouts = total_knockouts * first_round_percentage
    result = first_round_knockouts
    return result

print(solution())