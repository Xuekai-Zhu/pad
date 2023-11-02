def solution():
    # Calculate the current ages of the three siblings
    eldest_age = 20
    second_child_age = eldest_age - 5
    third_child_age = second_child_age - 5

    # Calculate the total of their ages 10 years from now
    total_age = (eldest_age + 10) + (second_child_age + 10) + (third_child_age + 10)
    result = total_age
    return result

print(solution())