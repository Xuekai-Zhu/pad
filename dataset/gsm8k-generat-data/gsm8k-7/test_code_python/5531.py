def solution():
    days_in_hospital = 3
    bed_cost_per_day = 900
    specialist_cost_per_hour = 250
    num_specialists = 2
    specialist_time_per_day = 30   # 2 specialists x 15 minutes each
    ambulance_cost = 1800

    # Calculate the cost of the hospital stay
    hospital_cost = days_in_hospital * bed_cost_per_day

    # Calculate the cost of the specialist consultations
    specialist_cost = (specialist_cost_per_hour / 60) * specialist_time_per_day * num_specialists * days_in_hospital

    # Calculate the total medical bill
    total_bill = hospital_cost + specialist_cost + ambulance_cost
    result = total_bill
    return result

print(solution())