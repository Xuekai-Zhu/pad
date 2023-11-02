def solution():
    """One student on a field trip counted 12 squirrels. Another counted a third more squirrels than the first student. How many squirrels did both students count combined?"""
    # Define the number of squirrels counted by the first student
    squirrels_first_student = 12

    # Calculate the number of squirrels counted by the second student
    squirrels_second_student = squirrels_first_student * (1 + 1/3)

    # Calculate the total number of squirrels counted
    total_squirrels = squirrels_first_student + squirrels_second_student

    # return the result
    result = total_squirrels
    return result

print(solution())