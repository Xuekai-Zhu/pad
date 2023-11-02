def solution():
     monthly_fee = 45
     overage_rate = .25
     total_bill = 65
     overage_gb = (total_bill - monthly_fee) / overage_rate
     result = overage_gb
     return result

print(solution())