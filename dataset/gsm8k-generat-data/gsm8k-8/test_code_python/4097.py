def solution():
    # Calculate the number of poets at the party
    poets = 120 + 50

    # Calculate the total number of poets and tree huggers
    poets_and_treehuggers = poets + 120

    # Calculate the number of singers
    singers = 400 - poets_and_treehuggers

    result = singers
    return result

print(solution())