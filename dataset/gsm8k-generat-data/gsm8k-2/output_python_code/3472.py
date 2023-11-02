def solution():
    """Tricia ordered three dozen eggs. She will use 1/4 of them for making crepes, and 2/3 of the remaining for making cupcakes. How many eggs are left to make sunny-side-up eggs for breakfast?"""
    total_eggs = 3 * 12
    crepe_eggs = total_eggs // 4
    remaining_eggs = total_eggs - crepe_eggs
    cupcake_eggs = (2/3) * remaining_eggs
    sunny_eggs = remaining_eggs - cupcake_eggs
    result = sunny_eggs
    return result

print(solution())