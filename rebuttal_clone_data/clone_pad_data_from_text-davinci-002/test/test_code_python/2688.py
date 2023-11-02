def solution():
     pinecones = 2000
     pinecones_eaten_by_reindeer = pinecones * 0.2
     pinecones_eaten_by_squirrels = pinecones_eaten_by_reindeer * 2
     pinecones_remaining = pinecones - pinecones_eaten_by_reindeer - pinecones_eaten_by_squirrels
     pinecones_collected = pinecones_remaining * 0.25
     pinecones_left = pinecones_remaining - pinecones_collected
     result = pinecones_left
     return result

print(solution())