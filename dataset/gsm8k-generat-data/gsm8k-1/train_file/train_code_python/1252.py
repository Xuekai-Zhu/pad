def solution():
    """Danai is decorating her house for Halloween. She puts 12 plastic skulls all around the house. She has 4 broomsticks, 1 for each side of the front and back doors to the house. She puts up 12 spiderwebs around various areas of the house. Danai puts twice as many pumpkins around the house as she put spiderwebs. She also places a large cauldron on the dining room table. If Danai has the budget left to buy 20 more decorations and has 10 left to put up, how many decorations will she put up in all?"""
    skulls = 12
    broomsticks = 4
    spiderwebs = 12
    pumpkins = spiderwebs * 2
    cauldrons = 1
    additional_decorations = 20
    decorations_left = 10
    total_decorations = skulls + broomsticks + spiderwebs + pumpkins + cauldrons + additional_decorations + decorations_left
    result = total_decorations
    return result

print(solution())