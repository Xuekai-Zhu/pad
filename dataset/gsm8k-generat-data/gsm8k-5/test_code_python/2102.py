def solution():
    salary = 2000 # Maria's monthly salary is $2000
    tax = 0.2 * salary # 20% of her salary goes to paying tax
    insurance = 0.05 * salary # 5% goes to insurance
    remaining_money = salary - tax - insurance # Calculate the remaining money after tax and insurance deductions
    utility_bills = 0.25 * remaining_money # A quarter of the remaining money is spent on utility bills
    money_left = remaining_money - utility_bills # Calculate the money left after utility bills payment
    result = money_left
    return result

print(solution())