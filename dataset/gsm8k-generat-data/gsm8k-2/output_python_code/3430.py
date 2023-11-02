def solution():
    """The school is hosting a race after school. The winner is the person who runs the most laps around the school in 12 minutes. 
    One lap around the school is 100 meters. The winner is awarded a gift certificate equal to $3.5 for every one hundred meters they run. 
    The winner runs 24 laps around the school. On average, how much did they earn per minute?"""
    laps = 24
    distance = laps * 100
    time = 12
    earnings = (distance / 100) * 3.5
    earnings_per_minute = earnings / time
    result = earnings_per_minute
    return result

print(solution())