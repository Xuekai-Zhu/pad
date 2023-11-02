def solution():
    num_roses = 3 * 12  # 3 dozen roses
    num_roses_given_away = num_roses / 2
    num_roses_in_vase = num_roses - num_roses_given_away

    num_wilted_roses = num_roses_in_vase / 3
    num_remaining_roses = num_roses_in_vase - num_wilted_roses
    result = num_remaining_roses
    return result

print(solution())