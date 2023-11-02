def solution():
    """Janet likes collecting action figures in her spare time. She currently owns 10 action figures and sells 6 of them to get 4 that are in better condition. Her brother then gives her his collection which is twice the size of what Janet has at the time. How many action figures does she now have in total?"""
    # Janet starts with 10 action figures
    initial_figures = 10

    # After selling 6 and buying 4, she has a net loss of 2 figures
    net_loss = 2

    # Janet's brother gives her a collection twice the size of what Janet has at the time
    brother_figures = initial_figures * 2

    # Janet's total number of figures is the sum of her initial figures, the net loss from selling and buying, and her brother's figures
    total_figures = initial_figures - net_loss + brother_figures

    # Display the total number of action figures Janet now has
    result = total_figures
    return result

print(solution())