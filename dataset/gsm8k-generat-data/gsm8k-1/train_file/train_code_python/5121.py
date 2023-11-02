def solution():
    """A firefighter's hose can deliver 20 gallons of water per minute. For a building fire that requires 4000 gallons of water to put out, how long will it take, in minutes, for a team of 5 firefighters, each with their own hose, to put out the fire?"""
    gallons_per_minute = 20
    total_gallons = 4000
    firefighters = 5
    time_in_minutes = total_gallons / (firefighters * gallons_per_minute)
    result = time_in_minutes
    return result

print(solution())