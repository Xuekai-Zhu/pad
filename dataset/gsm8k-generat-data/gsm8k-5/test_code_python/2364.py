def solution():
    total_students = 25  # There are 25 students in the class
    present_students = total_students - 1  # One student is absent
    average_score_needed = 75  # The average score needed to get a pizza party is 75%
    current_average_score = 77  # The current average score of the present students is 77%

    # Calculate the total score of the present students
    total_present_score = current_average_score * present_students

    # Calculate the minimum possible score the absent student needs to get to achieve an average score of 75%
    minimum_absent_score = ((average_score_needed * total_students) - total_present_score) / 1
    result = minimum_absent_score
    return result

print(solution())