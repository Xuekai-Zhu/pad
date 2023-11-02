def solution():
    # Convert 2 hours to minutes
    millennium_time = 2 * 60

    # Calculate Alpha Epsilon running time
    alpha_epsilon_time = millennium_time - 30

    # Calculate Beast of War running time
    beast_of_war_time = alpha_epsilon_time + 10

    # Convert Beast of War running time to minutes
    beast_of_war_time_minutes = beast_of_war_time * 60
    result = beast_of_war_time_minutes
    return result

print(solution())