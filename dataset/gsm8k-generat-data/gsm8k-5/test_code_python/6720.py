def solution():
    initial_collection = 10  # Janet starts with 10 action figures
    sold_figures = 6  # Janet sells 6 figures
    new_figures = 4  # Janet buys 4 new, better-condition figures
    remaining_figures = initial_collection - sold_figures + new_figures  # Janet is left with these figures
    brother_collection = 2 * remaining_figures  # Janet's brother gives her a collection twice the size of what Janet currently has

    # Calculate the total number of action figures Janet now has
    total_figures = remaining_figures + brother_collection
    result = total_figures
    return result

print(solution())