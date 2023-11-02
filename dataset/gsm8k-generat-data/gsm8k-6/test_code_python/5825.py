def solution():
    # Calculate the number of tomato slices needed for a family of 8
    slices_for_family = 20 * 8  # 20 slices make a meal for a single person, and there are 8 people in the family
    tomatoes_required = slices_for_family // 8  # each tomato yields 8 slices, so divide the total slices required by 8
    result = tomatoes_required
    return result

print(solution())