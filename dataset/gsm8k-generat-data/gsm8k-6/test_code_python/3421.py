def solution():
    # Total number of dogs Sam has
    total_dogs = 3 + 4  # Sam has 3 German Shepherds and 4 French Bulldogs

    # Number of German Shepherds Peter wants to buy
    german_shepherds_wanted = 3 * 3  # Peter wants to buy 3 times as many German Shepherds as Sam has

    # Number of French Bulldogs Peter wants to buy
    french_bulldogs_wanted = 2 * 4  # Peter wants to buy 2 times as many French Bulldogs as Sam has

    # Total number of dogs Peter wants to have
    total_peter_dogs = german_shepherds_wanted + french_bulldogs_wanted

    result = total_peter_dogs
    return result

print(solution())