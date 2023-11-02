def solution():
    # Define Düsseldorf's ranking and its air quality
    dusseldorf_ranking = 6
    smoggy_days = 50
    # Check if Düsseldorf has a small number of smoggy days each year
    if smoggy_days < 100:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())