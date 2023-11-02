def solution():
    """There are 2000 pinecones on the ground. 20% are eaten by reindeer. Twice as many are eaten by squirrels as reindeer. 25% of the remainder are collected to make fires. How many pinecones are left?"""
    pinecones = 2000
    reindeer_eaten = 0.2 * pinecones
    squirrels_eaten = 2 * reindeer_eaten
    remaining_pinecones = pinecones - reindeer_eaten - squirrels_eaten
    collected_for_fires = 0.25 * remaining_pinecones
    left_pinecones = remaining_pinecones - collected_for_fires
    result = left_pinecones
    return result

print(solution())