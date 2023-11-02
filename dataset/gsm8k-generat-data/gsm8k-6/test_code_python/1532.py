def solution():
    total_nails = 400  # total number of nails in the container
    used_for_kitchen = 0.3 * total_nails  # number of nails used for kitchen repairs
    remaining_nails = total_nails - used_for_kitchen  # number of nails remaining after kitchen repairs
    used_for_fence = 0.7 * remaining_nails  # number of nails used for fence repairs
    remaining_nails = remaining_nails - used_for_fence  # number of nails remaining after fence repairs
    result = remaining_nails
    return result

print(solution())