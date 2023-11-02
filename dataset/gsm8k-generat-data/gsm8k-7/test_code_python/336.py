def solution():
    num_cakes = 2
    num_slices_per_cake = 8
    slices_given_away = (num_cakes * num_slices_per_cake) / 4
    remaining_slices = (num_cakes * num_slices_per_cake) - slices_given_away
    slices_given_to_family = remaining_slices / 3
    remaining_slices -= slices_given_to_family
    remaining_slices -= 3  # Alex eats 3 slices
    result = remaining_slices
    return result

print(solution())