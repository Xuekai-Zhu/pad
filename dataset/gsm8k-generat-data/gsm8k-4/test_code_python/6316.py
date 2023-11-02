def solution():
    """John won $155250 in the lottery and decided to give one-thousandth of the $155250 to each of the top 100 students in his college. Calculate the total amount received by the hundred students of his college."""
    # Define the total amount won in the lottery
    total_amount = 155250

    # Calculate the amount to be given to each student
    amount_per_student = total_amount / 1000

    # Calculate the total amount received by the hundred students
    total_received = amount_per_student * 100

    # return the result
    result = total_received
    return result

print(solution())