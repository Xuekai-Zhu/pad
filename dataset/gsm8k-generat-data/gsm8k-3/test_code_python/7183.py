def solution():
    """A coal-powered train is traveling towards a faraway city when the conductor realizes that he forgot to restock the train's coal supply at the last station.  The train is traveling on a one-way track, so the conductor has no other option but to continue moving forward towards the city.  The train can travel 5 miles for every 2 pounds of coal that it consumes.  If the train has 160 pounds of coal remaining, how far can the train travel before it runs out of fuel?"""
    # Define the number of miles per 2 pounds of coal
    MILES_PER_COAL = 5

    # Define the remaining coal supply
    remaining_coal = 160

    # Calculate the distance the train can travel
    distance = MILES_PER_COAL * (remaining_coal // 2)

    # Display the distance the train can travel
    result = distance
    return result

print(solution())