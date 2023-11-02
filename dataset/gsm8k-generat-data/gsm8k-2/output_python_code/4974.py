def solution():
    """Angela has a collection of 24 pieces of rare action figures. She sold off a quarter of them at the pawnshop and gave one-third of the remainder to her daughter. How many does she have left?"""
    initial_figures = 24
    sold_figures = initial_figures / 4
    remaining_figures = initial_figures - sold_figures
    daughter_figures = remaining_figures / 3
    final_figures = remaining_figures - daughter_figures
    result = final_figures
    return result

print(solution())