def solution():
    """John decides to build a program capable of identifying cancer cells. He gets initial funding of $100,000 for the first 5 months of research. His research ends up taking 10 times that long and every month after those first 5 took 50% more funding per month. How much did his research cost?"""
    initial_funding = 100000
    research_time = 10
    funding_increase = 0.5
    total_funding = initial_funding
    for i in range(1, research_time):
        if i <= 5:
            total_funding += initial_funding
        else:
            total_funding += total_funding * funding_increase
    result = total_funding
    return result

print(solution())