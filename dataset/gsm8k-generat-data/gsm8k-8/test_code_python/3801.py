def solution():
    # Calculate the number of animals in Safari National Park
    safari_lions = 100
    safari_snakes = safari_lions / 2
    safari_giraffes = safari_snakes - 10
    safari_total = safari_lions + safari_snakes + safari_giraffes

    # Calculate the number of animals in Savanna National Park
    savanna_lions = 2 * safari_lions
    savanna_snakes = 3 * safari_snakes
    savanna_giraffes = safari_giraffes + 20
    savanna_total = savanna_lions + savanna_snakes + savanna_giraffes

    result = savanna_total
    return result

print(solution())