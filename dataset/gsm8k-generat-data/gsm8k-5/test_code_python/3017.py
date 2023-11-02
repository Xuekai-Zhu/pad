def solution():
    mandy_age = 3
    brother_age = mandy_age * 4
    sister_age = brother_age - 5

    # Calculate the age difference between Mandy and her sister
    age_difference = sister_age - mandy_age
    result = abs(age_difference)  # Use abs() to ensure a positive answer
    return result

print(solution())