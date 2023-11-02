def solution():
    """Martha collected 90 cans while Diego collected 10 more than half the cans collected by Martha. If both of them should collect a total of 150 cans for their project, how many more cans do they need to collect?"""
    # Number of cans Martha collected
    cans_martha = 90

    # Number of cans Diego collected
    cans_diego = (1/2)*cans_martha + 10

    # Total number of cans they should collect
    total_cans = 150

    # Number of cans they still need to collect
    cans_remaining = total_cans - (cans_martha + cans_diego)

    result = cans_remaining
    return result

print(solution())