def solution():
     fiona_hours = 40
     john_hours = 30
     jeremy_hours = 25
     fiona_salary = fiona_hours * 20
     john_salary = john_hours * 20
     jeremy_salary = jeremy_hours * 20
     boss_expense = fiona_salary + john_salary + jeremy_salary
     result = boss_expense
     return result

print(solution())