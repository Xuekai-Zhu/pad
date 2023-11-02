def solution():
    """John won $155250 in the lottery and decided to give one-thousandth of the $155250 to each of the top 100 students in his college. Calculate the total amount received by the hundred students of his college."""
    lottery_winnings = 155250
    n_students = 100
    amount_per_student = lottery_winnings / 1000 / n_students
    total_amount = amount_per_student * n_students
    result = total_amount
    return result

print(solution())