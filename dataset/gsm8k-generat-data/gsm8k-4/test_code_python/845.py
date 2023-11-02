def solution():
    """In a show, there can be 5 actors at a time. Every actor is in the show for about 15 minutes, and then another 5 actors come in. How many actors can there be on the show in 1 hour?"""
    # Define the number of actors that can participate in the show at a time
    actors_per_show = 5

    # Calculate the number of shows in 1 hour
    shows_per_hour = 60 // 20  # 60 minutes divided by 20 minutes per show (15 minutes for actors + 5 minutes for transition)

    # Calculate the total number of actors that can participate in the show in 1 hour
    total_actors = shows_per_hour * actors_per_show

    # Return the result
    result = total_actors
    return result

print(solution())