def solution():
    # Find the number of pinecones eaten by reindeer
    reindeer_eaten = 2000 * 0.2

    # Find the number of pinecones eaten by squirrels
    squirrel_eaten = 2 * reindeer_eaten

    # Find the remainder after pinecones are eaten by reindeer, squirrels
    remainder = 2000 - reindeer_eaten - squirrel_eaten

    # Find the number of pinecones collected for fires
    collected_for_fire = 0.25 * remainder

    # Find the number of pinecones remaining
    remaining_pinecones = remainder - collected_for_fire

    result = remaining_pinecones
    return result

print(solution())