def solution():
    """Martha collected 90 cans while Diego collected 10 more than half the cans collected by Martha. If both of them should collect a total of 150 cans for their project, how many more cans do they need to collect?"""
    martha_cans = 90
    diego_cans = (martha_cans / 2) + 10
    total_cans = 150
    cans_needed = total_cans - (martha_cans + diego_cans)
    result = cans_needed
    return result

print(solution())