def solution():
    """Danai is decorating her house for Halloween. She puts 12 plastic skulls all around the house. She has 4 broomsticks, 1 for each side of the front and back doors to the house. She puts up 12 spiderwebs around various areas of the house. Danai puts twice as many pumpkins around the house as she put spiderwebs. She also places a large cauldron on the dining room table. If Danai has the budget left to buy 20 more decorations and has 10 left to put up, how many decorations will she put up in all?"""
    # Define the number of decorations Danai puts up
    num_skulls = 12
    num_broomsticks = 4
    num_spiderwebs = 12
    num_pumpkins = num_spiderwebs * 2
    num_cauldrons = 1

    # Calculate the total number of decorations Danai puts up
    total_decorations = num_skulls + num_broomsticks + num_spiderwebs + num_pumpkins + num_cauldrons

    # Add the additional decorations she bought and has left to put up
    total_decorations += 20 + 10

    # Display the total number of decorations
    result = total_decorations
    return result

print(solution())