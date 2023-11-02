def solution():
    """Tricia ordered three dozen eggs. She will use 1/4 of them for making crepes, and 2/3 of the remaining for making cupcakes. How many eggs are left to make sunny-side-up eggs for breakfast?"""
    # Convert the number of dozens to the number of eggs
    total_eggs = 3 * 12

    # Calculate the number of eggs used for making crepes
    crepes_eggs = total_eggs * (1/4)

    # Calculate the remaining eggs
    remaining_eggs = total_eggs - crepes_eggs

    # Calculate the number of eggs used for making cupcakes
    cupcakes_eggs = remaining_eggs * (2/3)

    # Calculate the number of eggs left for making sunny-side-up eggs
    sunny_eggs = remaining_eggs - cupcakes_eggs

    result = sunny_eggs
    return result

print(solution())