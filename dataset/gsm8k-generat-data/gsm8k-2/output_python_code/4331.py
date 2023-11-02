def solution():
    """Bill and Jean are both cleaning out their garages. Bill makes a certain number of trips to the dump and Jean makes that many trips plus 6. If they make 40 trips total, how many trips does Jean make?"""
    total_trips = 40
    # Let x be the number of trips that Bill makes
    x = (total_trips - 6) / 2
    # Jean makes x + 6 trips
    jean_trips = x + 6
    result = jean_trips
    return result

print(solution())