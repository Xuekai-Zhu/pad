def solution():
    """Billy is counting the rings in two trees. Weather fluctuations in this area mean that each tree's rings are in groups of two fat rings and four thin rings. If Billy counts 70 ring groups in the first tree and 40 ring groups in the second tree, how much older is the first tree? (Trees grow 1 ring per year.)"""
    fat_rings_per_group = 2
    thin_rings_per_group = 4
    rings_per_group = fat_rings_per_group + thin_rings_per_group
    rings_in_first_tree = rings_per_group * 70
    rings_in_second_tree = rings_per_group * 40
    age_difference = (rings_in_first_tree - rings_in_second_tree) / 2
    result = age_difference
    return result

print(solution())