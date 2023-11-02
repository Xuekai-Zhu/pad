def solution():
    """A squirrel had stashed 210 acorns to last him the three winter months. It divided the pile into thirds, one for each month, and then took some from each third, leaving 60 acorns for each winter month. The squirrel combined the ones it took to eat in the first cold month of spring before plants were in bloom again. How many acorns does the squirrel have to eat at the beginning of spring?"""
    total_acorns = 210
    acorns_per_month = total_acorns / 3
    acorns_left_per_month = 60
    acorns_eaten_per_month = acorns_per_month - acorns_left_per_month
    acorns_to_eat_in_spring = acorns_eaten_per_month * 3
    result = acorns_to_eat_in_spring
    return result

print(solution())