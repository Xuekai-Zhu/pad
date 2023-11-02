def solution():
    # Define Scruffy's weight
    scruffy_weight = 12

    # Calculate Muffy's weight
    muffy_weight = scruffy_weight - 3

    # Calculate Puffy's weight
    puffy_weight = muffy_weight + 5

    # Calculate the total weight of Puffy and Muffy
    puffy_muffy_weight = puffy_weight + muffy_weight
    result = puffy_muffy_weight
    return result

print(solution())