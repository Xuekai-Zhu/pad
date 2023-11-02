def solution():
    """Danai is decorating her house for Halloween. She puts 12 plastic skulls all around the house. She has 4 broomsticks, 1 for each side of the front and back doors to the house. She puts up 12 spiderwebs around various areas of the house. Danai puts twice as many pumpkins around the house as she put spiderwebs. She also places a large cauldron on the dining room table. If Danai has the budget left to buy 20 more decorations and has 10 left to put up, how many decorations will she put up in all?"""
    # Define the number of each type of decoration
    skulls = 12
    broomsticks = 4
    spiderwebs = 12
    pumpkins = spiderwebs * 2
    cauldrons = 1

    # Calculate the number of decorations Danai has already put up
    decorations_put_up = skulls + broomsticks + spiderwebs + pumpkins + cauldrons

    # Calculate the number of decorations Danai has left to put up
    decorations_left_to_put_up = 10

    # Calculate the total number of decorations Danai will put up
    total_decorations = decorations_put_up + decorations_left_to_put_up

    # Add the number of decorations Danai plans to buy to the total
    total_decorations += 20

    result = total_decorations
    return result

print(solution())