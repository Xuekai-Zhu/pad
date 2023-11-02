def solution():
    # Define the host's name and status of the show
    host_name = "Bob Ross"
    producing_new_episodes = False
    # Check if the host is still alive and if the show is producing new episodes
    if host_name == "Bob Ross" and not producing_new_episodes:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())