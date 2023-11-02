def solution():
    num_jumping_jacks = 12
    num_pushups = 8
    num_situps = 20

    # Calculate the total number of exercises Emmett did
    total_exercises = num_jumping_jacks + num_pushups + num_situps

    # Calculate the percentage that pushups make up of total exercises
    pushup_percentage = (num_pushups / total_exercises) * 100

    result = pushup_percentage
    return result

print(solution())