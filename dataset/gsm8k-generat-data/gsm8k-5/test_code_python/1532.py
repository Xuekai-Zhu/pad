def solution():
    total_nails = 400
    used_for_kitchen = total_nails * 0.3  # 30% of nails used for kitchen repairs
    remaining_nails = total_nails - used_for_kitchen
    used_for_fence = remaining_nails * 0.7  # 70% of remaining nails used for fence repairs
    remaining_nails = remaining_nails - used_for_fence

    result = remaining_nails
    return result

print(solution())