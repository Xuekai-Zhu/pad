def solution():
    
    starting_figures = 10
    sold_figures = 6
    remaining_figures = starting_figures - sold_figures + 4
    brother_figures = remaining_figures * 2
    total_figures = remaining_figures + brother_figures
    result = total_figures
    return result

print(solution())