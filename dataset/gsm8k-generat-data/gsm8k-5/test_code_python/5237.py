def solution():
    distance_to_school = 0.5  # Wanda walks 0.5 miles to school
    distance_from_school = 0.5  # Wanda walks 0.5 miles back from school
    days_per_week = 5  # Wanda walks to school 5 days a week
    weeks = 4  # Wanda wants to know how many miles she will walk in 4 weeks

    # Calculate the total distance Wanda walks in a day
    total_distance_per_day = distance_to_school + distance_from_school

    # Calculate the total distance Wanda walks in a week
    total_distance_per_week = total_distance_per_day * days_per_week

    # Calculate the total distance Wanda walks in 4 weeks
    total_distance_per_four_weeks = total_distance_per_week * weeks
    result = total_distance_per_four_weeks
    return result

print(solution())