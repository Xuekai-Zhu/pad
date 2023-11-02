def solution():
    """Quinton is looking to add 4 fruit trees to his backyard. He wants to plant 2 apple trees that will be 10 feet wide each and need 12 feet between them. The peach trees will be closer to the house and will grow to be 12 feet wide and will need 15 feet between each tree. All told, how much space will these trees take up in his yard?"""
    apple_tree_width = 10
    apple_tree_spacing = 12
    peach_tree_width = 12
    peach_tree_spacing = 15
    total_space_taken = (2 * apple_tree_width) + apple_tree_spacing + (2 * peach_tree_width) + (3 * peach_tree_spacing)
    result = total_space_taken
    return result

print(solution())