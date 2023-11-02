def solution():
    initial_passengers = 124
    passengers_off_in_Texas = 58
    passengers_on_in_Texas = 24
    passengers_off_in_North_Carolina = 47
    passengers_on_in_North_Carolina = 14
    crew_members = 10
    passengers_in_Virginia = initial_passengers + passengers_on_in_Texas - passengers_off_in_Texas + passengers_on_in_North_Carolina - passengers_off_in_North_Carolina + crew_members
    result = passengers_in_Virginia
    return result

print(solution())