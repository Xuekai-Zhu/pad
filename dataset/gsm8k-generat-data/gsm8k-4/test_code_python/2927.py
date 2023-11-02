def solution():
    """A shoe company sells $4000 worth of shoes every month. If they want to make $60000 in an entire year how many more dollars per month should they make selling shoes?"""
    # Define the total amount to be made in a year
    annual_target = 60000

    # Define the current monthly sales
    monthly_sales = 4000

    # Calculate the additional monthly sales needed to reach the annual target
    additional_sales = (annual_target - (monthly_sales * 12)) / 12

    # return the result
    result = additional_sales
    return result

print(solution())