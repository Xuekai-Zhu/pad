def solution():
    num_dozen_eggs = 3
    num_eggs = num_dozen_eggs * 12

    # Calculate the number of eggs used for making crepes
    crepe_eggs = num_eggs * (1/4)

    # Calculate the number of eggs remaining after making crepes
    remaining_eggs = num_eggs - crepe_eggs

    # Calculate the number of eggs used for making cupcakes
    cupcake_eggs = remaining_eggs * (2/3)

    # Calculate the number of eggs remaining after making cupcakes
    remaining_eggs = remaining_eggs - cupcake_eggs

    result = remaining_eggs
    return result

print(solution())