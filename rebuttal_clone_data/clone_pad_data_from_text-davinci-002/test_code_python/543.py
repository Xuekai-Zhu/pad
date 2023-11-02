def solution():
    number_of_students = 25
    full_payment = 50
    partial_payment = full_payment / 2
    total_payment = (number_of_students * full_payment) - (partial_payment * 4)
    result = total_payment
    return result

print(solution())