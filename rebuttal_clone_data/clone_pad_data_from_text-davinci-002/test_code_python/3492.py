def solution():
     total_bills = 150
     num_10_bills = 50
     num_20_bills = 4
     num_5_bills = total_bills - (num_10_bills + (num_20_bills * 2))
     result = num_5_bills + num_10_bills + num_20_bills
     return result

print(solution())