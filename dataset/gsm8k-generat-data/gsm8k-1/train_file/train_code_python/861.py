def solution():
    """5 squirrels collected 575 acorns. If each squirrel needs 130 acorns to get through the winter, how many more acorns does each squirrel need to collect?"""
    total_acorns = 575
    num_squirrels = 5
    acorns_per_squirrel = 130
    acorns_needed = num_squirrels * acorns_per_squirrel
    acorns_leftover = total_acorns - acorns_needed
    acorns_needed_per_squirrel = acorns_per_squirrel - (acorns_leftover / num_squirrels)
    result = acorns_needed_per_squirrel
    return result

print(solution())