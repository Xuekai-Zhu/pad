def solution():
    """A company has 100 employees. 60% of the employees drive to work. Of the employees who don't drive to work, half take public transportation. How many employees use public transportation to get to work?"""
    # Define the total number of employees
    total_employees = 100

    # Calculate the number of employees who drive to work
    driving_employees = total_employees * 0.6

    # Calculate the number of employees who don't drive to work
    nondriving_employees = total_employees - driving_employees

    # Calculate the number of employees who take public transportation
    public_transportation_employees = nondriving_employees / 2

    # return the result
    result = public_transportation_employees
    return result

print(solution())