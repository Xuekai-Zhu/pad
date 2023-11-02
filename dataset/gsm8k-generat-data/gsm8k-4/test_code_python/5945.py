def solution():
    """Milly is making croissants. She needs to fold the dough 4 times, which takes 5 minutes each time, then let it rest for 75 minutes each time. If mixing the ingredients takes 10 minutes and baking the croissants takes 30 minutes, how many hours does the whole process take?"""
    # Define the time it takes to fold the dough and let it rest
    fold_rest_time = (5 + 75) * 4

    # Define the time it takes to mix the ingredients and bake the croissants
    mix_bake_time = 10 + 30

    # Add the two times together
    total_time = fold_rest_time + mix_bake_time

    # Convert the total time to hours
    hours = total_time / 60

    # Return the result
    result = hours
    return result

print(solution())