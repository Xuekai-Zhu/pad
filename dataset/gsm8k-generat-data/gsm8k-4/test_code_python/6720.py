def solution():
    """Janet likes collecting action figures in her spare time. She currently owns 10 action figures and sells 6 of them to get 4 that are in better condition. Her brother then gives her his collection which is twice the size of what Janet has at the time. How many action figures does she now have in total?"""
    # Define the initial number of action figures
    initial_figures = 10

    # Sell 6 figures and acquire 4 new ones
    current_figures = initial_figures - 6 + 4

    # Add her brother's collection, which is twice the size of what she had before
    final_figures = current_figures + (initial_figures * 2)

    # return the result
    result = final_figures
    return result

print(solution())