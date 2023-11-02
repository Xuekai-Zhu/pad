def solution():
    """The population of Port Perry is seven times as many as the population of Wellington. The population of Port Perry is 800 more than the population of Lazy Harbor. If Wellington has a population of 900, how many people live in Port Perry and Lazy Harbor combined?"""
    wellington_pop = 900
    portperry_pop = 7 * wellington_pop
    lazyharbor_pop = portperry_pop - 800
    total_pop = portperry_pop + lazyharbor_pop
    result = total_pop
    return result

print(solution())