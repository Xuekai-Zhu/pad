def solution():
    trout_weight = 8
    bass_weight = 2
    num_bass = 6
    salmon_weight = 12
    num_salmon = 2
    serving_size = 2

    # Calculate the total weight of all fish caught
    total_weight = trout_weight + (bass_weight * num_bass) + (salmon_weight * num_salmon)

    # Calculate the number of servings of fish
    num_servings = total_weight // serving_size

    result = num_servings
    return result

print(solution())