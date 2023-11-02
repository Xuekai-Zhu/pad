def solution():
    former_salary = 45000  # The teacher's former job paid $45,000 per year
    raise_percent = 20  # The parents offered the teacher a 20% raise
    new_salary = former_salary * (1 + raise_percent / 100)  # Calculate the new salary after the raise

    # Calculate the total cost of hiring the teacher for all 9 kids
    total_cost = new_salary / 9

    result = total_cost
    return result

print(solution())