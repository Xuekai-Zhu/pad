def solution():
    eldest_age = 20
    sibling_gap = 5

    # Calculate the ages of the other two siblings
    second_child_age = eldest_age - sibling_gap
    third_child_age = second_child_age - sibling_gap

    # Calculate the total of the ages of the three siblings 10 years from now
    total_age_10_years_from_now = (eldest_age + 10) + (second_child_age + 10) + (third_child_age + 10)
    result = total_age_10_years_from_now
    return result

print(solution())