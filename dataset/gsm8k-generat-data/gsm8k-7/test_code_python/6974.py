def solution():
    num_members = 4
    breakfast_slices_per_member = 3
    snack_slices_per_member = 2
    slices_per_loaf = 12
    num_loaves = 5

    # Calculate the total number of slices consumed by all members per day
    total_slices_per_day = (breakfast_slices_per_member + snack_slices_per_member) * num_members

    # Calculate the total number of slices consumed by all members in the family for the 5 loaves of bread
    total_slices_per_5_loaves = total_slices_per_day * slices_per_loaf * num_loaves

    # Calculate the number of days the 5 loaves of bread will last for the family
    days_5_loaves_will_last = total_slices_per_5_loaves / (total_slices_per_day * num_members)
    result = days_5_loaves_will_last
    return result

print(solution())