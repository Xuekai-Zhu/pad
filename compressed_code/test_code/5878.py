def solution():
    
    thank_you_cards = 3
    bills = 2
    rebates = bills + 3
    job_applications = rebates * 2
    electric_bill = 2
    total_envelopes = thank_you_cards + bills + rebates + job_applications + electric_bill
    total_stamps = total_envelopes - electric_bill + 1
    result = total_stamps
    return result

print(solution())