def solution():
    """Johnson owns a hectare cornfield that can yield 80 corn every two months, while his neighbor owns a two-hectare cornfield and each hectare can yield twice the amount as Johnson. How much corn can they harvest altogether after six months?"""
    # Define the yield of Johnson's cornfield per hectare every 2 months
    johnson_yield = 80

    # Calculate the yield of the neighbor's cornfield per hectare every 2 months
    neighbor_yield = johnson_yield * 2 * 2

    # Calculate the total yield of Johnson's cornfield after 6 months (3 two-month periods)
    johnson_total_yield = johnson_yield * 3

    # Calculate the total yield of the neighbor's cornfield after 6 months (3 two-month periods)
    neighbor_total_yield = neighbor_yield * 2 * 3

    # Calculate the total yield of both cornfields after 6 months
    total_yield = johnson_total_yield + neighbor_total_yield

    result = total_yield
    return result

print(solution())