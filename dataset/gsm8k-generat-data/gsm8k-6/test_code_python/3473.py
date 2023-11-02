def solution():
    # Convert three dozens of eggs to actual number of eggs
    total_eggs = 3 * 12  

    # Calculate the number of eggs used for making crepes
    crepe_eggs = total_eggs * (1/4)  

    # Calculate the remaining eggs after making crepes
    remaining_eggs = total_eggs - crepe_eggs  

    # Calculate the number of eggs used for making cupcakes
    cupcake_eggs = remaining_eggs * (2/3)  

    # Calculate the number of eggs left for making sunny-side-up eggs
    sunny_eggs = remaining_eggs - cupcake_eggs 

    result = sunny_eggs
    return result

print(solution())