def solution():
    """An apple tree has three times as many apples as the number of plums on a plum tree. If Damien picks 3/5 of the fruits from the trees, calculate the total number of plums and apples remaining on the tree if there were 180 apples on the apple tree before Damien picked any of the fruits."""
    apple_count = 180
    plum_count = apple_count / 3
    total_fruits = apple_count + plum_count
    remaining_fruits = total_fruits * (2 / 5)
    remaining_apples = remaining_fruits * (3 / 4)
    remaining_plums = remaining_fruits * (1 / 4)
    result = remaining_apples + remaining_plums
    return result

print(solution())