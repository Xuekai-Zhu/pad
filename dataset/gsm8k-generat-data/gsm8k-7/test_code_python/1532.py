def solution():
    total_nails = 400
    used_on_kitchen = (30 / 100) * total_nails
    remaining_nails = total_nails - used_on_kitchen
    used_on_fence = (70 / 100) * remaining_nails
    nails_remaining = remaining_nails - used_on_fence
    result = nails_remaining
    return result

print(solution())