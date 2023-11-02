def solution():
    
    total_money = 150
    num_10_bills = 5
    num_20_bills = 4
    total_10_bills = num_10_bills * 10
    total_20_bills = num_20_bills * 20
    total_5_bills = total_money - total_10_bills - total_20_bills
    num_5_bills = total_5_bills // 5
    total_bills = num_5_bills + num_10_bills + num_20_bills
    result = total_bills
    return result

print(solution())