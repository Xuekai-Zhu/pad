def solution():
    """Lauryn owns a computer company that employs men and women in different positions in the company.
    How many men does he employ if there are 20 fewer men than women and 180 people working for Lauryn?"""
    # Define the total number of employees working for Lauryn's company
    total_employees = 180

    # Calculate the number of women employees, using the fact that there are 20 fewer men than women
    women_employees = (total_employees + 20) / 2

    # Calculate the number of men employees
    men_employees = total_employees - women_employees

    # Return the number of men employees
    result = men_employees
    return result

print(solution())