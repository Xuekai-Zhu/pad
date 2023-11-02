def solution():
    # Calculate the total gallons of water delivered per minute by the team of firefighters
    gallons_per_minute = 20 * 5  # each firefighter has their own hose

    # Calculate the time it will take to deliver 4000 gallons of water
    time_in_minutes = 4000 / gallons_per_minute
    result = time_in_minutes
    return result

print(solution())