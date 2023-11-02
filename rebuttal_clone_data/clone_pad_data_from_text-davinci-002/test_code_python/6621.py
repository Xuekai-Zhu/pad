def solution():
    normal_complaints = 120
    complaints_short_staffed = normal_complaints * (1/3)
    complaints_self_checkout_broken = complaints_short_staffed * 1.2
    complaints_for_3_days = complaints_self_checkout_broken * 3
    result = complaints_for_3_days
    return result

print(solution())