def solution():
    """The moon is made of 50% iron, 20% carbon, and the remainder is other elements. Mars weighs twice as much as the moon, but has the exact same composition. If Mars is 150 tons of other elements, how many tons does the moon weigh?"""
    mars_other_elements = 150
    moon_weight = (2 * mars_other_elements) / 0.3
    result = moon_weight
    return result

print(solution())