def solution():
    """At a pool party, there are 4 pizzas cut into 12 slices each. If the guests eat 39 slices, how many slices are left?"""
    total_slices = 4 * 12
    eaten_slices = 39
    remaining_slices = total_slices - eaten_slices
    result = remaining_slices
    return result

print(solution())