def solution():
    """John won $155250 in the lottery and decided to give one-thousandth of the $155250  to each of the top 100 students in his college. Calculate the total amount received by the hundred students of his college."""
    # Calculate the amount each student will receive
    per_student = 155250 * 0.001

    # Calculate the total amount received by the top 100 students
    total_amount = per_student * 100

    # Display the total amount received
    result = total_amount
    return result

print(solution())