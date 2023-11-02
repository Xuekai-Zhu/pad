def solution():
    num_burgers = 5
    num_friends = 4
    slices_per_burger = 2
    slices_given = 1 + 2 + 3 + 3  # The first and second friends got 1 and 2 slices, respectively. Then the third and fourth friends got 3 slices each.
    total_slices = num_burgers * slices_per_burger
    slices_left = total_slices - slices_given
    result = slices_left
    return result

print(solution())