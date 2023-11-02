def solution():
    """The running time of Beast of War: Armoured Command is 10 minutes longer than that of Alpha Epsilon, which is 30 minutes shorter than that of Millennium. If Millennium runs for 2 hours, what is the running time of Beast of War: Armoured Command in minutes?"""
    millennium_runtime = 2*60 # in minutes
    alpha_epsilon_runtime = millennium_runtime - 30
    beast_of_war_runtime = alpha_epsilon_runtime + 10
    result = beast_of_war_runtime
    return result

print(solution())