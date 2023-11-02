def solution():
    """A coal-powered train is traveling towards a faraway city when the conductor realizes that he forgot to restock the train's coal supply at the last station. The train is traveling on a one-way track, so the conductor has no other option but to continue moving forward towards the city. The train can travel 5 miles for every 2 pounds of coal that it consumes. If the train has 160 pounds of coal remaining, how far can the train travel before it runs out of fuel?"""
    miles_per_coal = 5/2
    remaining_coal = 160
    distance_traveled = miles_per_coal * remaining_coal
    result = distance_traveled
    return result

print(solution())