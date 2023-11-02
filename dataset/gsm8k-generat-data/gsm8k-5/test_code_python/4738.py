def solution():
    total_pinecones = 2000  # There are 2000 pinecones on the ground
    reindeer_eaten = 0.2 * total_pinecones  # 20% are eaten by reindeer
    squirrel_eaten = 2 * reindeer_eaten  # Twice as many are eaten by squirrels as reindeer
    remaining_pinecones = total_pinecones - reindeer_eaten - squirrel_eaten
    # Calculate the remaining pinecones after eaten by reindeer and squirrels
    collected_for_fires = 0.25 * remaining_pinecones  # 25% of the remainder are collected to make fires
    remaining_pinecones = remaining_pinecones - collected_for_fires
    result = remaining_pinecones
    return result

print(solution())