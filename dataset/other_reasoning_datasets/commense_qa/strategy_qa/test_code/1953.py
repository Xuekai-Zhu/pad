def solution():
    uninsured = True
    cost_of_ct_scan = 5000
    insured = True
    
    if uninsured and cost_of_ct_scan > 0 and not insured:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())