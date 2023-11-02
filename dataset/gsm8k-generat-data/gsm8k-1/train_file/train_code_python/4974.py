def solution():
    """Angela has a collection of 24 pieces of rare action figures. She sold off a quarter of them at the pawnshop and gave one-third of the remainder to her daughter. How many does she have left?"""
    total_figures = 24
    sold_figures = total_figures // 4
    remaining_figures = total_figures - sold_figures
    daughter_figures = remaining_figures // 3
    final_figures = remaining_figures - daughter_figures
    result = final_figures
    return result

print(solution())