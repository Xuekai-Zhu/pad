def solution():
    
    job_a_pay = 15 * 2000
    job_a_tax = job_a_pay * 0.2
    job_b_pay = 42000
    job_b_tax = 6000 * 0.1
    job_b_tax_net = job_b_tax * 0.9
    net_pay = job_b_pay - job_b_tax_net
    difference = net_pay - job_a_tax_net
    result = difference
    return result

print(solution())