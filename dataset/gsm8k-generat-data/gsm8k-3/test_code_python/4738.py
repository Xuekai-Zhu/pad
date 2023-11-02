def solution():
    """There are 2000 pinecones on the ground. 20% are eaten by reindeer. Twice as many are eaten by squirrels as reindeer. 25% of the remainder are collected to make fires. How many pinecones are left?"""
    # Define the percentage of pinecones eaten by reindeer and squirrels
    REINDEER_PERCENTAGE = 0.2
    SQUIRREL_PERCENTAGE = REINDEER_PERCENTAGE * 2

    # Calculate the number of pinecones eaten by reindeer
    reindeer_eaten = int(2000 * REINDEER_PERCENTAGE)

    # Calculate the number of pinecones eaten by squirrels
    squirrel_eaten = int(2000 * SQUIRREL_PERCENTAGE)

    # Calculate the number of pinecones remaining
    remaining_pinecones = 2000 - reindeer_eaten - squirrel_eaten

    # Calculate the number of pinecones collected for fires
    collected_pinecones = int(remaining_pinecones * 0.25)

    # Calculate the final number of pinecones remaining
    final_pinecones = remaining_pinecones - collected_pinecones

    # Display the final number of pinecones
    result = final_pinecones
    return result

print(solution())