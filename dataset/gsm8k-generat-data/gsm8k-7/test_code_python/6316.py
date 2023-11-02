def solution():
    total_prize_money = 155250
    num_top_students = 100
    amount_per_student = total_prize_money * 0.001

    # Calculate the total amount received by the top 100 students
    total_amount_received = amount_per_student * num_top_students
    result = total_amount_received
    return result

print(solution())