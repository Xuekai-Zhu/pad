def solution():
    skulls = 12  # Danai puts 12 plastic skulls all around the house
    broomsticks = 4  # Danai has 4 broomsticks
    spiderwebs = 12  # Danai puts 12 spiderwebs around the house
    pumpkins = 2 * spiderwebs  # Danai puts twice as many pumpkins around the house as she put spiderwebs
    cauldron = 1  # Danai places a large cauldron on the dining room table
    additional_decorations = 20  # Danai has the budget left to buy 20 more decorations
    remaining_decorations = 10  # Danai has 10 left to put up

    # Calculate the total number of decorations
    total_decorations = skulls + broomsticks + spiderwebs + pumpkins + cauldron + additional_decorations + remaining_decorations
    result = total_decorations
    return result

print(solution())