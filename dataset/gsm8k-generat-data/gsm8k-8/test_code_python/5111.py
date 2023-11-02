def solution():
    # Calculate the ages of the other two siblings
    second_child_age = 20 - 5
    third_child_age = second_child_age - 5

    # Calculate the total of their ages in 10 years
    total_age_in_10_years = (20 + 10) + (second_child_age + 10) + (third_child_age + 10)

    result = total_age_in_10_years
    return result

print(solution())