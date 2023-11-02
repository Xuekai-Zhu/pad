def solution():
    
    eldest_age_now = 20
    age_difference = 5
    second_child_age = eldest_age_now - age_difference
    third_child_age = second_child_age - age_difference
    total_age_in_10_years = (eldest_age_now + 10) + (second_child_age + 10) + (third_child_age + 10)
    result = total_age_in_10_years
    return result

print(solution())