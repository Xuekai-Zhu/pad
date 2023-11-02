def solution():
    """My new house has 12 medium ceiling lights but I have seen small and large ceiling lights in other rooms. The small ones require 1 bulb, the medium ones require 2, and the large ones need 3 bulbs. How many bulbs should I buy if my wife says she saw twice as many large ceiling lights as medium ceiling lights and ten more small lights than medium ones?"""
    # Define the number of medium ceiling lights
    medium_lights = 12

    # Calculate the number of small and large ceiling lights
    large_lights = medium_lights * 2
    small_lights = medium_lights + 10

    # Calculate the total number of bulbs needed
    total_bulbs = (2 * medium_lights) + (3 * large_lights) + small_lights

    # Display the total number of bulbs needed
    result = total_bulbs
    return result

print(solution())