def solution():
    johnson_yield = 80  # Johnson's cornfield can yield 80 corn every two months
    neighbor_yield = johnson_yield * 2 * 2  # Neighbor's cornfield yields twice the amount as Johnson, and he has 2 hectares

    # Calculate the total yield for Johnson after six months
    johnson_total_yield = johnson_yield * 3  # Johnson harvests corn every two months, so he will harvest 3 times in 6 months

    # Calculate the total yield for Johnson's neighbor after six months
    neighbor_total_yield = neighbor_yield * 3  # Neighbor harvests corn every two months, so he will harvest 3 times in 6 months

    # Calculate the total yield for both Johnson and his neighbor after six months
    total_yield = johnson_total_yield + neighbor_total_yield
    result = total_yield
    return result

print(solution())