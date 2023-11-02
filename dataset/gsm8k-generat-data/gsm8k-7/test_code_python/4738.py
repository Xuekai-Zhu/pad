def solution():
    num_pinecones = 2000
    reindeer_eaten = 0.2
    squirrel_eaten = reindeer_eaten * 2
    collected_for_fire = 0.25

    # Calculate the number of pinecones eaten by reindeer
    pinecones_reindeer_eaten = num_pinecones * reindeer_eaten

    # Calculate the number of pinecones eaten by squirrels
    pinecones_squirrel_eaten = pinecones_reindeer_eaten * 2

    # Calculate the total number of pinecones remaining
    pinecones_remaining = num_pinecones - pinecones_reindeer_eaten - pinecones_squirrel_eaten

    # Calculate the number of pinecones collected for fire
    pinecones_collected_for_fire = pinecones_remaining * collected_for_fire

    # Calculate the final number of pinecones remaining
    pinecones_left = pinecones_remaining - pinecones_collected_for_fire
    result = pinecones_left
    return result

print(solution())