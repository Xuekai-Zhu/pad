def solution():
    """A boat carrying 20 sheep, 10 cows and 14 dogs capsized.  3 of the sheep drowned.  Twice as many cows drowned as did sheep.  All of the dogs made it to shore.  How many total animals made it to the shore?"""
    # Define the initial number of animals
    sheep = 20
    cows = 10
    dogs = 14

    # Update the number of animals that drowned
    sheep -= 3
    cows -= 2 * 3

    # Calculate the number of animals that made it to shore
    animals_on_shore = sheep + cows + dogs

    # return the result
    result = animals_on_shore
    return result

print(solution())