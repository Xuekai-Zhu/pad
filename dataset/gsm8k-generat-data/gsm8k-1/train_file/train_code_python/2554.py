def solution():
    """The moon is made of 50% iron, 20% carbon, and the remainder is other elements. Mars weighs twice as much as the moon, but has the exact same composition. If Mars is 150 tons of other elements, how many tons does the moon weigh?"""
    mars_other = 150
    mars_total = mars_other / 0.3
    moon_total = mars_total / 2
    moon_iron = moon_total * 0.5
    moon_carbon = moon_total * 0.2
    moon_other = moon_total * 0.3
    result = moon_total
    return result

print(solution())