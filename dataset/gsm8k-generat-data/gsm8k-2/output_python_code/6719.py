def solution():
    """Janet likes collecting action figures in her spare time. She currently owns 10 action figures and sells 6 of them to get 4 that are in better condition. Her brother then gives her his collection which is twice the size of what Janet has at the time. How many action figures does she now have in total?"""
    starting_figures = 10
    sold_figures = 6
    remaining_figures = starting_figures - sold_figures + 4
    brother_figures = remaining_figures * 2
    total_figures = remaining_figures + brother_figures
    result = total_figures
    return result

print(solution())