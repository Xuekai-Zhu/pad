def solution():
    
    normal_complaints = 120
    short_staffed_increase = normal_complaints * (1/3)
    broken_self_checkout_increase = (normal_complaints + short_staffed_increase) * 0.2
    total_complaints = normal_complaints + short_staffed_increase + broken_self_checkout_increase
    total_complaints *= 3  
    result = total_complaints
    return result

print(solution())