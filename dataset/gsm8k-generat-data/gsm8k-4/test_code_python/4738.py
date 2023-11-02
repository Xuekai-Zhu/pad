def solution():
    """There are 2000 pinecones on the ground. 20% are eaten by reindeer. Twice as many are eaten by squirrels as reindeer. 25% of the remainder are collected to make fires. How many pinecones are left?"""
    # Define the initial number of pinecones
    total_pinecones = 2000

    # Calculate the number of pinecones eaten by reindeer
    reindeer_pinecones = total_pinecones * 0.2

    # Calculate the number of pinecones eaten by squirrels
    squirrel_pinecones = reindeer_pinecones * 2

    # Calculate the number of pinecones remaining after reindeer and squirrel eating them
    remaining_pinecones = total_pinecones - reindeer_pinecones - squirrel_pinecones

    # Calculate the number of pinecones collected for firewood
    firewood_pinecones = remaining_pinecones * 0.25

    # Calculate the number of pinecones left
    left_pinecones = remaining_pinecones - firewood_pinecones

    # return the result
    result = left_pinecones
    return result

print(solution())