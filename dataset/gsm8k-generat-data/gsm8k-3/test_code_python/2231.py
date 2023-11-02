def solution():
    """A married couple and their 6 children are ordering some pizza. If the couple want 3 slices each and the children want 1 slice each, how many 4-slice pizzas should they order?"""
    # Define the number of adults and children
    adults = 2
    children = 6

    # Calculate the total number of slices needed
    total_slices = (adults * 3) + children

    # Calculate the number of 4-slice pizzas needed
    pizzas = (total_slices // 4) + 1

    # Display the number of pizzas needed
    result = pizzas
    return result

print(solution())