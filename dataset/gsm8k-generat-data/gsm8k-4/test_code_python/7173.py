def solution():
    """In the fall, 20,000 high school students apply to Harvard University for college. In the spring, 5% of those 20,000 students are accepted to the university. Of the students who are accepted, 90% choose to attend the university, and the other 10% choose to go to other schools. How many students choose to attend Harvard University?"""
    # Define the total number of students who applied to Harvard
    total_students = 20000

    # Calculate the number of students who were accepted to Harvard
    accepted_students = total_students * 0.05

    # Calculate the number of students who chose to attend Harvard
    attending_students = accepted_students * 0.9

    # return the result
    result = attending_students
    return result

print(solution())