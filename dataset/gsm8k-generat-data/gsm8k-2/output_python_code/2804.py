def solution():
    """Brittany has 3 gerbils: Puffy, Muffy, and Scruffy. Puffy weighs 5 ounces more than Muffy. Muffy weighs 3 ounces less than Scruffy. If Scruffy weighs 12 ounces, how much would the scale indicate, in ounces, if Brittany put Puffy and Muffy on the scale?"""
    scruffy_weight = 12
    muffy_weight = scruffy_weight - 3
    puffy_weight = muffy_weight + 5
    total_weight = muffy_weight + puffy_weight
    result = total_weight
    return result

print(solution())