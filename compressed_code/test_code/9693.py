def solution():
    
    total_figures = 24
    sold_figures = total_figures // 4
    remaining_figures = total_figures - sold_figures
    daughter_figures = remaining_figures // 3
    final_figures = remaining_figures - daughter_figures
    result = final_figures
    return result

print(solution())