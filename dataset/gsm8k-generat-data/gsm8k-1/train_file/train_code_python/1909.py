def solution():
    """Johnson owns a hectare cornfield that can yield 80 corn every two months, while his neighbor owns a two-hectare cornfield and each hectare can yield twice the amount as Johnson. How much corn can they harvest altogether after six months?"""
    johnson_yield = 80
    johnson_harvest = johnson_yield * 3 # Johnson harvests every 2 months
    neighbor_harvest = (2 * johnson_harvest) * 3 # Neighbor has 2 hectares and yields twice as much as Johnson
    total_harvest = johnson_harvest + neighbor_harvest
    result = total_harvest
    return result

print(solution())