def solution():
    actors_per_set = 5  # There are 5 actors in each set
    set_duration = 15 / 60  # Each set lasts for 15 minutes, converted to hours
    total_duration = 1  # The total duration of the show is 1 hour

    # Calculate the number of sets in the total duration of the show
    total_sets = total_duration // set_duration

    # Calculate the total number of actors in the show
    total_actors = total_sets * actors_per_set

    result = total_actors
    return result

print(solution())