def solution():
    # Calculate the number of knockouts Rocky had
    knockouts = 0.5 * 190  # 50% of his fights were knockouts
    first_round_knockouts = 0.2 * knockouts  # 20% of the knockouts were in the first round
    result = first_round_knockouts
    return result

print(solution())