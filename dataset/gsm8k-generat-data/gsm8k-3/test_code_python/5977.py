def solution():
    """A group of parents get together and decide to hire a private school teacher to quit his job and teach their children.  His former job paid 45,000 per year and they offered him a 20% raise.  If there are 9 kids how much does each parent have to pay?"""
    # Define the teacher's former salary and the percentage raise
    FORMER_SALARY = 45000
    PERCENT_RAISE = 0.2

    # Calculate the teacher's new salary
    new_salary = FORMER_SALARY * (1 + PERCENT_RAISE)

    # Divide the new salary by the number of parents (which is assumed to be the same as the number of kids)
    cost_per_parent = new_salary / 9

    # Display the cost per parent
    result = cost_per_parent
    return result

print(solution())