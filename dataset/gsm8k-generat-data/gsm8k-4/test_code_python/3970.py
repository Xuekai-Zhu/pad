def solution():
    """Carla adds a can of chilis, two cans of beans, and 50% more tomatoes than beans to a normal batch of chili. If she makes a quadruple batch, how many cans of food does she need?"""
    # Define the ingredients in a normal batch of chili
    normal_chili = {
        "chilis": 1,
        "beans": 2,
        "tomatoes": 3,
    }

    # Calculate the quantity of ingredients needed for a quadruple batch
    quadruple_chili = {
        "chilis": normal_chili["chilis"] * 4,
        "beans": normal_chili["beans"] * 4 + 2,
        "tomatoes": normal_chili["beans"] * 4 * 1.5,
    }

    # Calculate the total number of cans needed
    total_cans = sum(quadruple_chili.values())

    # return the result
    result = total_cans
    return result

print(solution())