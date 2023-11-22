def solution():
    
    # Define Tim's salary and bonus amount
    salary = 20000
    bonus = salary / 2

    # Calculate Tim's new salary after the promotion
    new_salary = salary * 1.05

    # Calculate Tim's new salary after the bonus
    new_salary += bonus

    # Calculate Tim's annual salary after the promotion
    annual_salary = new_salary * 12

    # Display Tim's annual salary
    result = annual_salary
    return result

print(solution())