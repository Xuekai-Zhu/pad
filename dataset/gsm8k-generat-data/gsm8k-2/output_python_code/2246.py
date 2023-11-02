def solution():
    """Billy is counting the rings in two trees. Weather fluctuations in this area mean that each tree's rings are in groups of two fat rings and four thin rings. If Billy counts 70 ring groups in the first tree and 40 ring groups in the second tree, how much older is the first tree? (Trees grow 1 ring per year.)"""
    fat_rings = 2
    thin_rings = 4
    rings_per_group = fat_rings + thin_rings
    tree1_ring_groups = 70
    tree2_ring_groups = 40
    tree1_ring_count = tree1_ring_groups * rings_per_group
    tree2_ring_count = tree2_ring_groups * rings_per_group
    tree1_age = tree1_ring_count // 2
    tree2_age = tree2_ring_count // 2
    age_difference = tree1_age - tree2_age
    result = age_difference
    return result

print(solution())