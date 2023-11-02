def solution():
    """Dijana and Anis live near a lake, and every weekend they go out rowing into the lake. On a Sunday morning, both went out rowing, and Dijana rowed for 50 miles the whole day. Anis rowed 1/5 times more miles than Dijana. Calculate the total distance the two of them rowed on that day."""
    dijana_miles = 50
    anis_miles = dijana_miles + (dijana_miles * (1/5))
    total_distance = dijana_miles + anis_miles
    result = total_distance
    return result

print(solution())