def solution():
    daily_distance = 10  # Shane drives 10 miles each day
    semester_length = 80  # The semester is 80 days long

    # Calculate the total distance Shane drives in the semester
    total_distance = daily_distance * 2 * semester_length  # Shane drives to and from school each day
    result = total_distance
    return result

print(solution())