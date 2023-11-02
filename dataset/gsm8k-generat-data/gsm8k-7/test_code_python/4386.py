def solution():
    num_babysitting_jobs = 4
    babysitting_pay = 30

    num_car_washes = 5
    car_wash_pay = 12

    # Calculate the total amount earned from babysitting jobs
    total_babysitting_pay = num_babysitting_jobs * babysitting_pay

    # Calculate the total amount earned from car washes
    total_car_wash_pay = num_car_washes * car_wash_pay

    # Calculate the total amount raised
    total_raised = total_babysitting_pay + total_car_wash_pay
    result = total_raised
    return result

print(solution())