def solution():
    # Convert 2 hours to minutes
    millennium_runtime = 2 * 60

    # Calculate the runtime of Alpha Epsilon and Beast of War: Armoured Command
    alpha_epsilon_runtime = millennium_runtime - 30
    beast_of_war_runtime = alpha_epsilon_runtime + 10

    # Return the runtime of Beast of War: Armoured Command in minutes
    result = beast_of_war_runtime
    return result

print(solution())