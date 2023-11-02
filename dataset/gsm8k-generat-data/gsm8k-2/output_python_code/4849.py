def solution():
    """While bird watching, Gabrielle saw 5 robins, 4 cardinals, and 3 blue jays. Chase saw 2 robins, 3 blue jays, and 5 cardinals. How many more birds, in percentage, did Gabrielle see than Chase?"""
    gabrielle_birds = 5 + 4 + 3
    chase_birds = 2 + 3 + 5
    diff_birds = gabrielle_birds - chase_birds
    percentage_more = (diff_birds / chase_birds) * 100
    result = percentage_more
    return result

print(solution())