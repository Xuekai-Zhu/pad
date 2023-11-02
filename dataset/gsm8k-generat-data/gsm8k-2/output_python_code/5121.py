def solution():
    """A firefighter's hose can deliver 20 gallons of water per minute. For a building fire that requires 4000 gallons of water to put out, how long will it take, in minutes, for a team of 5 firefighters, each with their own hose, to put out the fire?"""
    hose_capacity = 20
    total_water_needed = 4000
    firefighters = 5
    total_hoses = firefighters
    total_water_per_minute = hose_capacity * total_hoses
    time_to_put_out_fire = total_water_needed / total_water_per_minute
    result = time_to_put_out_fire
    return result

print(solution())