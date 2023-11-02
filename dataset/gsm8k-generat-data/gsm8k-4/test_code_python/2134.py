def solution():
    """Martha collected 90 cans while Diego collected 10 more than half the cans collected by Martha. If both of them should collect a total of 150 cans for their project, how many more cans do they need to collect?"""
    # Define the number of cans collected by Martha
    martha_cans = 90

    # Calculate the number of cans collected by Diego
    diego_cans = (martha_cans / 2) + 10

    # Calculate the total number of cans collected by both
    total_cans = martha_cans + diego_cans

    # Calculate the number of cans needed to reach the target
    cans_needed = 150 - total_cans

    result = cans_needed
    return result

print(solution())