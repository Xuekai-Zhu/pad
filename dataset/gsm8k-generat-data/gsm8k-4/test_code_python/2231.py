def solution():
    """A married couple and their 6 children are ordering some pizza. If the couple want 3 slices each and the children want 1 slice each, how many 4-slice pizzas should they order?"""
    # Define the number of slices the couple wants
    couple_slices = 3 * 2

    # Define the number of slices the children want
    children_slices = 6 * 1

    # Calculate the total number of slices needed
    total_slices = couple_slices + children_slices

    # Calculate the number of pizzas needed
    pizzas = total_slices // 4 + (total_slices % 4 > 0)

    # Return the result
    result = pizzas
    return result

print(solution())