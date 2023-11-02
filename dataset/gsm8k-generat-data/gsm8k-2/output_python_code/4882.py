def solution():
    """Tim has to go to the doctor for a sporting injury. He gets an MRI which costs $1200. The doctor needs to examine it for 30 minutes and charges $300 per hour. There is also a $150 fee just for being seen. Insurance covered 80% how much did he pay?"""
    mri_cost = 1200
    exam_time = 0.5 # 30 minutes
    exam_cost_per_hour = 300
    exam_cost = exam_time * exam_cost_per_hour
    seen_fee = 150
    total_cost = mri_cost + exam_cost + seen_fee
    insurance_coverage = 0.8
    amount_paid = total_cost * (1 - insurance_coverage)
    result = amount_paid
    return result

print(solution())