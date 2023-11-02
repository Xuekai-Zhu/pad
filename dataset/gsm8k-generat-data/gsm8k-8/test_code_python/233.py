def solution():
    # Define the number of push-ups per set and the total number of sets
    pushups_per_set = 15
    total_sets = 3

    # Calculate the total number of push-ups before getting tired
    total_pushups = pushups_per_set * total_sets

    # Calculate the number of push-ups in the last set after getting tired
    tired_pushups = 5

    # Calculate the final total number of push-ups
    final_pushups = total_pushups - tired_pushups
    result = final_pushups
    return result

print(solution())