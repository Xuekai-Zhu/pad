def solution():
    """Rocky boxed 190 fights in his career. 50 percent of his fights were knockouts, and 20 percent of the knockouts were in the first round. How many knockouts did Rocky have in the first round?"""
    total_fights = 190
    knockout_percent = 50
    first_round_percent = 20
    knockouts = total_fights * (knockout_percent / 100)
    first_round_knockouts = knockouts * (first_round_percent / 100)
    result = first_round_knockouts
    return result

print(solution())