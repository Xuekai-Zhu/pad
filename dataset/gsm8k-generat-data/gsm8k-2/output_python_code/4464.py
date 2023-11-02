def solution():
    """June found 2 birds nest with 5 eggs each in 1 tree and 1 nest with 3 eggs in another tree. There was also a nest with 4 eggs in her front yard. How many birds eggs did she find?"""
    eggs_in_tree1 = 2 * 5
    eggs_in_tree2 = 3
    eggs_in_front_yard = 4
    total_eggs = eggs_in_tree1 + eggs_in_tree2 + eggs_in_front_yard
    result = total_eggs
    return result

print(solution())