def solution():
    skulls = 12
    broomsticks = 4
    spiderwebs = 12
    pumpkins = spiderwebs * 2
    cauldron = 1
    additional_decorations = 20
    remaining_decorations = 10

    # Calculate the total number of decorations Danai has put up already
    total_decorations = skulls + broomsticks + spiderwebs + pumpkins + cauldron

    # Calculate the total number of decorations Danai will put up, including additional and remaining decorations
    total_decorations += additional_decorations + remaining_decorations
    result = total_decorations
    return result

print(solution())