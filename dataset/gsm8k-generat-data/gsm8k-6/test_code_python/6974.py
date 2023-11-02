def solution():
    # Calculate how many slices of bread are consumed per day
    slices_per_day = 4 * (3 + 2)  # 4 members, 3 slices for breakfast, 2 slices for snacks

    # Calculate how many slices of bread are consumed in 5 days
    total_slices = slices_per_day * 5

    # Calculate how many loaves of bread are needed for 5 days
    loaves_needed = total_slices / 12

    result = loaves_needed
    return result

print(solution())