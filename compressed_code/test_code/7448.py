def solution():
    
    salary = 2000
    tax = salary * 0.2
    insurance = salary * 0.05
    remaining_money = salary - tax - insurance
    utility_bills = remaining_money / 4
    final_money = remaining_money - utility_bills
    result = final_money
    return result

print(solution())