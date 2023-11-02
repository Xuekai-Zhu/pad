def solution():
    # Calculate the amount received by each of the top 100 students
    amount_per_student = 155250 * (1/1000) / 100  # one-thousandth of $155250 divided by 100 students
    total_amount = amount_per_student * 100  # total amount received by hundred students
    result = total_amount
    return result

print(solution())