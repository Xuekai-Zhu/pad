def solution():
    """Kelian has two recipes for preparing dishes, one having 20 instructions and the second one having twice as many instructions as the first one. How many instructions does Kelian have to read to prepare the two dishes?"""
    recipe1_instructions = 20
    recipe2_instructions = recipe1_instructions * 2
    total_instructions = recipe1_instructions + recipe2_instructions
    result = total_instructions
    return result

print(solution())