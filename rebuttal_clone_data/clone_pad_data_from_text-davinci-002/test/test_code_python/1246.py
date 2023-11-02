def solution():
    car_insurance_cost = 80
    Nancy_percent_payment = 40
    Nancy_payment = car_insurance_cost * (Nancy_percent_payment / 100)
    Nancy_payment_month = Nancy_payment * 12

    return Nancy_payment_month

print(solution())