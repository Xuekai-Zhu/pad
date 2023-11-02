def solution():
    tuition_fee = 90
    part_time_job_pay = 15
    scholarship_discount = 0.3
    num_months = 3

    # Calculate the total amount of scholarship discount
    scholarship_amount = tuition_fee * scholarship_discount

    # Calculate the remaining tuition fee after scholarship discount
    remaining_tuition_fee = tuition_fee - scholarship_amount

    # Calculate the total amount Bran earns from his part-time job
    total_job_pay = part_time_job_pay * num_months

    # Calculate the final amount Bran still needs to pay
    final_amount = remaining_tuition_fee - total_job_pay
    result = final_amount
    return result

print(solution())