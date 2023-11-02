def solution():
    # Calculate the number of pinecones eaten by reindeer
    reindeer_eaten = 0.2 * 2000

    # Calculate the number of pinecones eaten by squirrels
    squirrel_eaten = 2 * reindeer_eaten

    # Calculate the total number of pinecones eaten
    total_eaten = reindeer_eaten + squirrel_eaten

    # Calculate the number of pinecones remaining
    remaining_pinecones = 2000 - total_eaten

    # Calculate the number of pinecones collected for fires
    fire_pinecones = 0.25 * remaining_pinecones

    # Calculate the final number of pinecones remaining
    final_pinecones = remaining_pinecones - fire_pinecones

    result = final_pinecones
    return result

print(solution())