def solution():
    """Tim's car goes down in value by $1000 a year. He bought it for $20,000. How much is it worth after 6 years?"""
    # Define the initial value of the car and the annual decrease in value
    initial_value = 20000
    decrease_per_year = 1000

    # Calculate the value of the car after 6 years
    final_value = initial_value - (decrease_per_year * 6)

    # return the result
    result = final_value
    return result

print(solution())