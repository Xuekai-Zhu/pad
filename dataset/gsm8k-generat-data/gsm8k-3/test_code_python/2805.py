def solution():
    """Brittany has 3 gerbils: Puffy, Muffy, and Scruffy. Puffy weighs 5 ounces more than Muffy. Muffy weighs 3 ounces less than Scruffy. If Scruffy weighs 12 ounces, how much would the scale indicate, in ounces, if Brittany put Puffy and Muffy on the scale?"""
    # Define the weight of Scruffy
    SCRUFFY_WEIGHT = 12

    # Calculate the weight of Muffy
    muffy_weight = SCRUFFY_WEIGHT - 3

    # Calculate the weight of Puffy
    puffy_weight = muffy_weight + 5

    # Calculate the total weight of Puffy and Muffy
    total_weight = puffy_weight + muffy_weight

    # Display the total weight
    result = total_weight
    return result

print(solution())