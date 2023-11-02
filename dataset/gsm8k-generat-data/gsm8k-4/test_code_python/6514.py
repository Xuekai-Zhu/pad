def solution():
    """There are 500 students in a local high school. 40 percent are juniors. 70 percent of juniors are involved in sports. How many juniors are involved in sports?"""
    # Define the total number of students
    total_students = 500

    # Calculate the number of junior students
    junior_students = total_students * 0.4

    # Calculate the number of junior students involved in sports
    sports_juniors = junior_students * 0.7

    # Return the result
    result = sports_juniors
    return result

print(solution())