def solution():
    # Find Vikki's gross weekly earnings
    gross_earnings = 42 * 10  # hourly pay rate is $10 and Vikki worked for 42 hours

    # Find the total amount deducted from Vikki's weekly earnings
    total_deductions = 0.2 * gross_earnings + 0.05 * gross_earnings + 5  # 20% tax, 5% insurance and $5 union dues are deducted

    # Find Vikki's net weekly earnings
    net_earnings = gross_earnings - total_deductions
    result = net_earnings
    return result

print(solution())