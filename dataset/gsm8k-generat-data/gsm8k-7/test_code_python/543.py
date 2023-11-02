def solution():
    num_students = 25
    full_payment = 50
    half_payment = full_payment / 2
    num_half_pay = 4

    # Calculate the total amount gathered from students who paid full payment
    total_full_pay = (num_students - num_half_pay) * full_payment

    # Calculate the total amount gathered from students who paid half payment
    total_half_pay = num_half_pay * half_payment

    # Calculate the total amount gathered
    total_gathered = total_full_pay + total_half_pay
    result = total_gathered
    return result

print(solution())