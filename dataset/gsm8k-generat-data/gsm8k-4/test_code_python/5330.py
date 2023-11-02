def solution():
    """Steve makes 40000$ a year as a teacher. He loses 20 percent to taxes, 10 percent to healthcare, and 800$ to local union dues. How much money does Steve take home?"""
    # Define the initial salary of Steve
    salary = 40000

    # Calculate the amount of money lost to taxes
    taxes = salary * 0.2

    # Calculate the amount of money lost to healthcare
    healthcare = salary * 0.1

    # Calculate the total amount of money lost to taxes and healthcare
    deductions = taxes + healthcare + 800

    # Calculate the amount of money Steve takes home
    take_home_pay = salary - deductions

    result = take_home_pay
    return result

print(solution())