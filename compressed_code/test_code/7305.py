def solution():
    
    rate_donaldsons = 15
    rate_merck = 18
    rate_hille = 20
    hours_donaldsons = 7
    hours_merck = 6
    hours_hille = 3
    total_pay = rate_donaldsons * hours_donaldsons + rate_merck * hours_merck + rate_hille * hours_hille
    result = total_pay
    return result

print(solution())