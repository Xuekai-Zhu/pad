def solution():
    """Steve makes 40000$ a year as a teacher.  He loses 20 percent to taxes, 10 percent to healthcare, and 800$ to local union dues.  How much money does Steve take home?"""
    # Define the initial salary
    salary = 40000

    # Calculate the amount lost to taxes
    tax_loss = 0.2 * salary

    # Calculate the amount lost to healthcare
    healthcare_loss = 0.1 * salary

    # Calculate the total amount lost
    total_loss = tax_loss + healthcare_loss + 800

    # Calculate the amount Steve takes home
    take_home = salary - total_loss

    # Display the amount Steve takes home
    result = take_home
    return result

print(solution())