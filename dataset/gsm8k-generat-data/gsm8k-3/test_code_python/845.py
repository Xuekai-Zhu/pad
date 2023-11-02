def solution():
    """In a show, there can be 5 actors at a time. Every actor is in the show for about 15 minutes, and then another 5 actors come in. How many actors can there be on the show in 1 hour?"""
    # Define the number of actors per group and the time for each group
    ACTORS_PER_GROUP = 5
    TIME_PER_GROUP = 15 # in minutes

    # Calculate the number of groups in 1 hour
    num_groups_hour = 60 / TIME_PER_GROUP

    # Calculate the total number of actors in 1 hour
    total_actors_hour = num_groups_hour * ACTORS_PER_GROUP

    # Display the total number of actors in 1 hour
    result = total_actors_hour
    return result

print(solution())