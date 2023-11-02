def solution():
    """A firefighter's hose can deliver 20 gallons of water per minute.  For a building fire that requires 4000 gallons of water to put out, how long will it take, in minutes, for a team of 5 firefighters, each with their own hose, to put out the fire?"""
    # Define the water delivery rate per hose
    RATE_PER_HOSE = 20  # gallons per minute

    # Define the total amount of water needed to put out the fire
    TOTAL_WATER_NEEDED = 4000  # gallons

    # Calculate the total water delivery rate of the team of firefighters
    total_rate = RATE_PER_HOSE * 5  # gallons per minute

    # Calculate the time needed to deliver the total amount of water
    time_needed = TOTAL_WATER_NEEDED / total_rate  # minutes

    # Display the time needed to put out the fire
    result = time_needed
    return result

print(solution())