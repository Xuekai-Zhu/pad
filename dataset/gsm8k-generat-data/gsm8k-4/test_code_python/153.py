def solution():
    """Tim's cat bit him. He decided to get himself and the cat checked out. His doctor's visits $300 and insurance covered 75%. His cat's visit cost $120 and his pet insurance covered $60. How much did he pay?"""
    # Calculate the amount Tim has to pay for his doctor's visit
    doctor_visit_cost = 300
    insurance_coverage = 0.75
    insurance_payment = doctor_visit_cost * insurance_coverage
    tim_payment = doctor_visit_cost - insurance_payment

    # Calculate the amount Tim has to pay for his cat's visit
    cat_visit_cost = 120
    insurance_coverage = 0.5
    insurance_payment = cat_visit_cost * insurance_coverage
    tim_cat_payment = cat_visit_cost - insurance_payment

    # Calculate the total cost Tim has to pay
    total_cost = tim_payment + tim_cat_payment

    result = total_cost
    return result

print(solution())