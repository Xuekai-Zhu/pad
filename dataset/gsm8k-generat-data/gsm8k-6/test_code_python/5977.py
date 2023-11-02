def solution():
    former_salary = 45000  # the teacher's former job paid 45,000 per year
    raise_amount = 0.2  # they offered him a 20% raise
    new_salary = former_salary + (raise_amount * former_salary)  # the new salary after the raise
    total_cost = new_salary / 9  # the total cost to be split among the 9 parents
    result = total_cost
    return result

print(solution())