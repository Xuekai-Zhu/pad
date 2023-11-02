def solution():
    milk_cow_provides = 16
    milk_consumed_by_daisys_kids = 0.75 * milk_cow_provides
    milk_left_over = milk_cow_provides - milk_consumed_by_daisys_kids
    milk_used_for_cooking = 0.50 * milk_left_over
    milk_left = milk_left_over - milk_used_for_cooking
    result = milk_left
    return result

print(solution())