def solution():
    """A firefighter's hose can deliver 20 gallons of water per minute. For a building fire that requires 4000 gallons of water to put out, how long will it take, in minutes, for a team of 5 firefighters, each with their own hose, to put out the fire?"""
    # Define the water required to put out the fire and the water delivered per minute by a single hose
    WATER_REQUIRED = 4000
    WATER_PER_MINUTE_PER_HOSE = 20

    # Calculate the total water delivered per minute by the team of firefighters
    total_water_per_minute = WATER_PER_MINUTE_PER_HOSE * 5

    # Calculate the time required to put out the fire
    time_required = WATER_REQUIRED / total_water_per_minute

    result = time_required
    return result

print(solution())