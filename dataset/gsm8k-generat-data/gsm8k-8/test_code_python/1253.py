def solution():
    # Define the number of each decoration Danai used
    skulls = 12
    broomsticks = 4
    spiderwebs = 12
    pumpkins = 2 * spiderwebs
    cauldrons = 1

    # Calculate the total number of decorations Danai used
    total_decorations = skulls + broomsticks + spiderwebs + pumpkins + cauldrons

    # Calculate the number of decorations Danai will buy and put up
    additional_decorations = 20 + 10

    # Calculate the total number of decorations Danai will use
    total_decorations += additional_decorations

    result = total_decorations
    return result

print(solution())