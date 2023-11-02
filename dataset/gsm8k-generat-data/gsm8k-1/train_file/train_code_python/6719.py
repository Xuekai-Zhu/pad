def solution():
    """Janet likes collecting action figures in her spare time. She currently owns 10 action figures and sells 6 of them to get 4 that are in better condition. Her brother then gives her his collection which is twice the size of what Janet has at the time. How many action figures does she now have in total?"""
    initial_collection = 10
    sold_figures = 6
    new_figures = 4
    remaining_figures = initial_collection - sold_figures + new_figures
    brother_collection = remaining_figures * 2
    total_figures = remaining_figures + brother_collection
    result = total_figures
    return result

print(solution())