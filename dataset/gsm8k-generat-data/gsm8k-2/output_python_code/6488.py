def solution():
    """A squirrel had stashed 210 acorns to last him the three winter months. It divided the pile into thirds, one for each month, and then took some from each third, leaving 60 acorns for each winter month. The squirrel combined the ones it took to eat in the first cold month of spring before plants were in bloom again. How many acorns does the squirrel have to eat at the beginning of spring?"""
    total_acorns = 210
    acorns_per_month = total_acorns / 3
    remaining_acorns = acorns_per_month - 60
    acorns_eaten_in_spring = (remaining_acorns * 3) + (total_acorns - acorns_per_month)
    result = acorns_eaten_in_spring
    return result

print(solution())