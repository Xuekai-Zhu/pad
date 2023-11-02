def solution():
    """An NGO contracted a construction company to build 2000 houses within one year. In the first half of the year, they built the first 3/5 units of the contracted number. Due to unavoidable circumstances, the company could only build an additional 300 units by October. How many units remain from the contracted number that the company is supposed to build?"""
    # Define the total number of units contracted to be built
    total_units = 2000

    # Calculate the number of units built in the first half of the year
    units_first_half = total_units * (3/5)

    # Calculate the number of units built by October
    units_by_october = units_first_half + 300

    # Calculate the remaining number of units to be built
    remaining_units = total_units - units_by_october

    # Display the remaining number of units to be built
    result = remaining_units
    return result

print(solution())