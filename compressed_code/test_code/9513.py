def solution():
    
    total_pinecones = 2000
    reindeer_eaten = total_pinecones * 0.20
    squirrel_eaten = reindeer_eaten * 2
    remaining_pinecones = total_pinecones - reindeer_eaten - squirrel_eaten
    fire_collected = remaining_pinecones * 0.25
    left_pinecones = remaining_pinecones - fire_collected
    result = left_pinecones
    return result

print(solution())