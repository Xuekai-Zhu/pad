def solution():
    total_sailors = 17
    num_inexperienced = 5
    inexperienced_pay = 10
    hours_per_week = 60
    weeks_per_month = 4

    num_experienced = total_sailors - num_inexperienced
    experienced_pay = inexperienced_pay * 1.2  # 1/5 more than inexperienced pay

    # Calculate the total monthly earnings of experienced sailors
    total_experienced_pay = num_experienced * experienced_pay * hours_per_week * weeks_per_month

    result = total_experienced_pay
    return result

print(solution())