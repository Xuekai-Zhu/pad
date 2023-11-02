def solution():
    """John won $155250 in the lottery and decided to give one-thousandth of the $155250 to each of the top 100 students in his college. Calculate the total amount received by the hundred students of his college."""
    total_amount = 155250
    num_students = 100
    amount_per_student = total_amount / 1000 / num_students
    total_received = amount_per_student * num_students
    result = total_received
    return result

print(solution())