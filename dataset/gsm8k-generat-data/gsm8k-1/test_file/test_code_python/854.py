def solution():
    """A plague infects ten people. Every day, each infected person infects six others. How many people are infected after three days?"""
    initial_infected = 10
    new_infected = 6
    days = 3
    total_infected = initial_infected * (new_infected**days)
    result = total_infected
    return result

print(solution())