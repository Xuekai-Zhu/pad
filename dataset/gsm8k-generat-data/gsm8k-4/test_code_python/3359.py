def solution():
    """Ben has two brothers. They can each eat 12 slices of pizza. They are ordering pizza for the night and want to make sure they get enough. The large pizzas have 14 slices and the small pizzas have 8. If they order 1 small pizza, how many large pizzas do they need to order?"""
    # Define the number of slices each person can eat
    slices_per_person = 12

    # Define the number of slices per small pizza and large pizza
    small_slices = 8
    large_slices = 14

    # Calculate the total number of slices needed for all three brothers
    total_slices = (slices_per_person * 3)

    # Calculate the number of slices provided by the small pizza
    small_pizza_slices = small_slices

    # Calculate the number of slices needed from the large pizzas
    large_pizza_slices_needed = total_slices - small_pizza_slices

    # Calculate the number of large pizzas needed
    large_pizzas_needed = large_pizza_slices_needed / large_slices

    # Round up to the nearest whole number of large pizzas
    large_pizzas_needed = int(large_pizzas_needed) + (large_pizzas_needed % 1 > 0)

    # return the result
    result = large_pizzas_needed
    return result

print(solution())