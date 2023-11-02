def solution():
    millennium_runtime = 2 * 60  # Millennium runs for 2 hours, or 120 minutes
    alpha_epsilon_runtime = millennium_runtime - 30  # Alpha Epsilon is 30 minutes shorter than Millennium
    beast_of_war_runtime = alpha_epsilon_runtime + 10  # Beast of War is 10 minutes longer than Alpha Epsilon

    # Convert the running time of Beast of War to minutes
    beast_of_war_runtime_minutes = beast_of_war_runtime * 60
    result = beast_of_war_runtime_minutes
    return result

print(solution())