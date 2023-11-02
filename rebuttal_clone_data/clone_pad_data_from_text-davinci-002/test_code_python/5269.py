def solution():
     mother_bills = [50, 20, 20, 10, 10, 10]
     father_bills = [50, 50, 50, 50, 20, 10]
     total_bills = mother_bills + father_bills
     total_fee = sum(total_bills)
     return total_fee

print(solution())