def solution():
     pay = 1120
     retirement_deduction = pay * .25
     tax_deduction = 100
     net_pay = pay - retirement_deduction - tax_deduction
     result = net_pay
     return result

print(solution())