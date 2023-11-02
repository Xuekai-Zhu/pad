def solution():
    """The moon is made of 50% iron, 20% carbon, and the remainder is other elements. Mars weighs twice as much as the moon, but has the exact same composition. If Mars is 150 tons of other elements, how many tons does the moon weigh?"""
    # Define the weights of iron, carbon, and other elements in the moon
    iron_moon = 0.5
    carbon_moon = 0.2
    other_moon = 0.3

    # Define the weight of other elements in Mars
    other_mars = 150

    # Calculate the total weight of Mars
    total_mars = other_mars / other_moon * (iron_moon + carbon_moon + other_moon)

    # Calculate the weight of the moon
    weight_moon = total_mars / 2

    # return the result
    result = weight_moon
    return result

print(solution())