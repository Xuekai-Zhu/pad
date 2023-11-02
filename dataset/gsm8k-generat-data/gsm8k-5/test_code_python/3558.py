def solution():
    total_fights = 190  # Rocky boxed 190 fights in his career
    knockout_percentage = 0.5  # 50% of his fights were knockouts
    first_round_percentage = 0.2  # 20% of the knockouts were in the first round

    # Calculate the total number of knockouts
    knockouts_total = total_fights * knockout_percentage

    # Calculate the number of knockouts in the first round
    knockouts_first_round = knockouts_total * first_round_percentage
    result = knockouts_first_round
    return result

print(solution())