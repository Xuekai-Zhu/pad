def solution():
    """The moon is made of 50% iron, 20% carbon, and the remainder is other elements. Mars weighs twice as much as the moon, but has the exact same composition. If Mars is 150 tons of other elements, how many tons does the moon weigh?"""
    # Define the composition of the moon and Mars
    IRON_COMPOSITION = 0.5
    CARBON_COMPOSITION = 0.2
    OTHER_COMPOSITION = 0.3

    # Define the weight of Mars
    mars_weight = 300 # since Mars weighs twice as much as the moon

    # Calculate the weight of the other elements in the moon
    moon_other_weight = mars_weight * OTHER_COMPOSITION - 150 

    # Calculate the total weight of the moon
    moon_weight = moon_other_weight / (IRON_COMPOSITION + CARBON_COMPOSITION)

    # Display the weight of the moon
    result = moon_weight
    return result

print(solution())