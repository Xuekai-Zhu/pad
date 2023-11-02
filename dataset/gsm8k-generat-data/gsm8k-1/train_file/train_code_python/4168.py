def solution():
    """An apple tree has three times as many apples as the number of plums on a plum tree. If Damien picks 3/5 of the fruits from the trees, calculate the total number of plums and apples remaining on the tree if there were 180 apples on the apple tree before Damien picked any of the fruits."""
    apples_before = 180
    plums_before = apples_before / 3
    total_fruits_before = apples_before + plums_before
    fruits_picked = total_fruits_before * 3/5
    apples_after = apples_before - fruits_picked/4
    plums_after = plums_before - fruits_picked/4
    result = apples_after + plums_after
    return result

print(solution())