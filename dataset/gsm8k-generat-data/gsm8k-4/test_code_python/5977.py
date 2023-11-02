def solution():
    """A group of parents get together and decide to hire a private school teacher to quit his job and teach their children. His former job paid 45,000 per year and they offered him a 20% raise. If there are 9 kids how much does each parent have to pay?"""
    # Define the teacher's former salary and the percentage raise
    former_salary = 45000
    percentage_raise = 0.2

    # Calculate the new salary with the percentage raise
    new_salary = former_salary * (1 + percentage_raise)

    # Calculate the total cost for the teacher's salary
    total_cost = new_salary / 9

    result = round(total_cost, 2)
    return result

print(solution())