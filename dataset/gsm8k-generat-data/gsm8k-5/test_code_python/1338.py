def solution():
    medium_lights = 12  # My new house has 12 medium ceiling lights
    small_lights = medium_lights + 10  # My wife saw 10 more small lights than medium ones
    large_lights = medium_lights * 2  # My wife saw twice as many large lights as medium ones

    # Calculate the total number of bulbs needed for each type of light
    bulbs_for_small_lights = small_lights * 1
    bulbs_for_medium_lights = medium_lights * 2
    bulbs_for_large_lights = large_lights * 3

    # Calculate the total number of bulbs needed
    total_bulbs = bulbs_for_small_lights + bulbs_for_medium_lights + bulbs_for_large_lights
    result = total_bulbs
    return result

print(solution())