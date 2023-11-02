def solution():
    num_days_per_week = 5
    oldest_child_servings_per_day = 2
    youngest_child_servings_per_day = 1
    num_servings_per_package = 30
    num_weeks = 4

    # Calculate the total number of servings of string cheese needed for both kids for 4 weeks
    total_servings = (oldest_child_servings_per_day + youngest_child_servings_per_day) * num_days_per_week * num_weeks

    # Calculate the total number of packages needed to provide enough servings
    total_packages = total_servings / num_servings_per_package

    result = total_packages
    return result

print(solution())