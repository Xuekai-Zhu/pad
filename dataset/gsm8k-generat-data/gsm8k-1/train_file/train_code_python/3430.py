def solution():
    """The school is hosting a race after school. The winner is the person who runs the most laps around the school in 12 minutes. One lap around the school is 100 meters. The winner is awarded a gift certificate equal to $3.5 for every one hundred meters they run. The winner runs 24 laps around the school. On average, how much did they earn per minute?"""
    time_in_minutes = 12
    laps_completed = 24
    distance_per_lap = 100
    total_distance = laps_completed * distance_per_lap
    dollars_per_100_meters = 3.5
    earnings = total_distance * (dollars_per_100_meters / 100)
    earnings_per_minute = earnings / time_in_minutes
    result = earnings_per_minute
    return result

print(solution())