def solution():
    """Johnson owns a hectare cornfield that can yield 80 corn every two months, while his neighbor owns a two-hectare cornfield and each hectare can yield twice the amount as Johnson. How much corn can they harvest altogether after six months?"""
    # Calculate Johnson's corn yield for 6 months
    johnson_yield = 80 * 3

    # Calculate the neighbor's corn yield for 6 months
    neighbor_yield = (80 * 2 * 2) * 3

    # Calculate the total corn yield
    total_yield = johnson_yield + neighbor_yield

    # Display the total corn yield
    result = total_yield
    return result

print(solution())