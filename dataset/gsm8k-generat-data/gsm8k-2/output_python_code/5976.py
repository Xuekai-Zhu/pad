def solution():
    """A group of parents get together and decide to hire a private school teacher to quit his job and teach their children. His former job paid 45,000 per year and they offered him a 20% raise. If there are 9 kids how much does each parent have to pay?"""
    former_salary = 45000
    raise_percentage = 0.2
    new_salary = former_salary * (1 + raise_percentage)
    num_parents = 9
    total_cost = new_salary / num_parents
    result = total_cost
    return result

print(solution())