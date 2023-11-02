def solution():
    """Johnson owns a hectare cornfield that can yield 80 corn every two months, while his neighbor owns a two-hectare cornfield and each hectare can yield twice the amount as Johnson. How much corn can they harvest altogether after six months?"""
    johnson_yield = 80
    neighbor_yield = 2 * johnson_yield * 2  # 2 hectares and twice the yield as Johnson's field
    total_yield = (johnson_yield * 3) + (neighbor_yield * 3)  # 6 months total
    result = total_yield
    return result

print(solution())