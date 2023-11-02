def solution():
    """A coal-powered train is traveling towards a faraway city when the conductor realizes that he forgot to restock the train's coal supply at the last station. The train is traveling on a one-way track, so the conductor has no other option but to continue moving forward towards the city. The train can travel 5 miles for every 2 pounds of coal that it consumes. If the train has 160 pounds of coal remaining, how far can the train travel before it runs out of fuel?"""
    # Define the fuel consumption rate in miles per pound of coal
    fuel_consumption_rate = 5 / 2

    # Calculate the total distance the train can travel based on the remaining coal supply
    total_distance = fuel_consumption_rate * 160

    # return the result
    result = total_distance
    return result

print(solution())