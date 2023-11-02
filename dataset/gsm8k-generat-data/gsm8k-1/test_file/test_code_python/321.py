def solution():
    """Jaime is a computer programmer for a company that currently has employed 100 people. Senior programmers are paid $400 more than junior programmers. If the number of Junior programmers is 2/5 of the total number of employees, and they are each paid $2000 per month, calculate the total amount of money the company pays to all the programmers per month."""
    total_employees = 100
    junior_percent = 0.4
    junior_programmers = int(total_employees * junior_percent)
    senior_programmers = total_employees - junior_programmers
    junior_salary = 2000
    senior_salary = junior_salary + 400
    total_salary = (junior_programmers * junior_salary) + (senior_programmers * senior_salary)
    result = total_salary
    return result

print(solution())