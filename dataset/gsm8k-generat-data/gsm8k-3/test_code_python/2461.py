def solution():
    """Tim's car goes down in value by $1000 a year. He bought it for $20,000. How much is it worth after 6 years?"""
    # Define the initial value and depreciation per year
    initial_value = 20000
    depreciation_per_year = 1000

    # Calculate the current value after 6 years
    current_value = initial_value - depreciation_per_year * 6

    # Display the current value
    result = current_value
    return result

print(solution())