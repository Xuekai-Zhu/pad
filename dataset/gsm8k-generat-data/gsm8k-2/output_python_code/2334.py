def solution():
    """A loaf of bread was sliced into 15. Ten friends bought 4 loaves of bread. If they all eat all 4 loaves equally, how many slices of bread did each of them eat?"""
    slices_per_loaf = 15
    total_slices = slices_per_loaf * 4
    num_friends = 10
    slices_per_friend = total_slices / num_friends
    result = slices_per_friend
    return result

print(solution())