def solution():
    """At a pool party, there are 4 pizzas cut into 12 slices each. If the guests eat 39 slices, how many slices are left?"""
    total_slices = 4 * 12
    slices_eaten = 39
    slices_left = total_slices - slices_eaten
    result = slices_left
    return result

print(solution())