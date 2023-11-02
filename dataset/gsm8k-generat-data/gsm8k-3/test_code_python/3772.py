def solution():
    """The running time of Beast of War: Armoured Command is 10 minutes longer than that of Alpha Epsilon, which is 30 minutes shorter than that of Millennium. If Millennium runs for 2 hours, what is the running time of Beast of War: Armoured Command in minutes?"""
    # Define the running times of Millennium and Alpha Epsilon in minutes
    millennium_time = 2 * 60
    alpha_epsilon_time = millennium_time - 30

    # Define the running time of Beast of War: Armoured Command
    beast_of_war_time = alpha_epsilon_time + 10

    # Convert the running time of Beast of War: Armoured Command to minutes
    beast_of_war_time_minutes = beast_of_war_time * 60

    # Display the running time of Beast of War: Armoured Command in minutes
    result = beast_of_war_time_minutes
    return result

print(solution())