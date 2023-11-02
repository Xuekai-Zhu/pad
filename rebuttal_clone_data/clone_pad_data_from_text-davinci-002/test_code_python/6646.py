def solution():
     bills_paid = [50, 50, 50, 10, 10]
     sum_of_bills = 0
     for bill in bills_paid:
         sum_of_bills = sum_of_bills + bill
     result = sum_of_bills
     return result

print(solution())