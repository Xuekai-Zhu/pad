def solution():
     five_bills = 4
     twenty_bills = 3
     ten_bills = (100 - (5 * five_bills) - (20 * twenty_bills)) / 10
     result = ten_bills
     return result

print(solution())