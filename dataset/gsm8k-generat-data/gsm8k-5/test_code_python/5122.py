def solution():
    water_delivery_rate = 20  # The hose can deliver 20 gallons of water per minute
    total_required_water = 4000  # The building fire requires 4000 gallons of water to put out
    firefighters = 5  # There are 5 firefighters in the team
    hoses_per_firefighter = 1  # Each firefighter has their own hose

    # Calculate the total water delivery rate of the team
    total_water_delivery_rate = water_delivery_rate * firefighters * hoses_per_firefighter

    # Calculate the time required to put out the fire
    time_required = total_required_water / total_water_delivery_rate
    result = time_required
    return result

print(solution())