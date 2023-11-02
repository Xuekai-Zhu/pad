def solution():
    # Define the number of eggs in three dozen
    eggs = 3 * 12

    # Calculate the number of eggs used for making crepes
    crepe_eggs = eggs * (1/4)

    # Calculate the remaining number of eggs
    remaining_eggs = eggs - crepe_eggs

    # Calculate the number of eggs used for making cupcakes
    cupcake_eggs = remaining_eggs * (2/3)

    # Calculate the number of eggs left for making sunny-side-up eggs
    sunny_eggs = remaining_eggs - cupcake_eggs

    result = sunny_eggs
    return result

print(solution())