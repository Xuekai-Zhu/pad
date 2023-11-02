def solution():
    """During the outbreak of the coronavirus, a company had to ramp up its toilet paper production three times more to cover the increased demand. If the company was producing 7000 toilet paper per day, calculate its total toilet paper production during March of 2020 after increasing its production."""
    initial_production = 7000
    increase_factor = 3
    total_production = initial_production * increase_factor * 31
    result = total_production
    return result

print(solution())