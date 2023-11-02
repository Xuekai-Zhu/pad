def solution():
    """Sam has 3 German Shepherds and 4 French Bulldogs. Peter wants to buy 3 times as many German Shepherds as Sam has and 2 times as many French Bulldogs as Sam has. How many dogs does Peter want to have?"""
    # Define the number of German Shepherds and French Bulldogs Sam has
    sam_shepherds = 3
    sam_bulldogs = 4

    # Calculate the number of German Shepherds and French Bulldogs Peter wants
    peter_shepherds = 3 * sam_shepherds
    peter_bulldogs = 2 * sam_bulldogs

    # Calculate the total number of dogs Peter wants
    total_dogs = peter_shepherds + peter_bulldogs

    # Display the total number of dogs Peter wants
    result = total_dogs
    return result

print(solution())