def solution():
    """My new house has 12 medium ceiling lights but I have seen small and large ceiling lights in other rooms.
    The small ones require 1 bulb, the medium ones require 2, and the large ones need 3 bulbs.
    How many bulbs should I buy if my wife says she saw twice as many large ceiling lights as medium ceiling lights and ten more small lights than medium ones?"""
    medium_lights = 12
    small_lights = medium_lights + 10
    large_lights = 2 * medium_lights
    total_bulbs = (medium_lights * 2) + small_lights + (large_lights * 3)
    result = total_bulbs
    return result

print(solution())