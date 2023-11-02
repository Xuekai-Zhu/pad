def solution():
    """One set of barrettes costs $3 each, and one comb costs $1 each. Kristine buys one set of barrettes and one comb. Crystal buys three sets of barrettes and one comb. How much do the two girls spend altogether?"""
    kristine_barrettes = 1
    kristine_comb = 1
    crystal_barrettes = 3
    crystal_comb = 1
    kristine_cost = kristine_barrettes * 3 + kristine_comb * 1
    crystal_cost = crystal_barrettes * 3 + crystal_comb * 1
    total_cost = kristine_cost + crystal_cost
    result = total_cost
    return result

print(solution())