def solution():
    # Define the number of years worked as a bartender and manager
    bartender_years = 9
    manager_years = 3.5

    # Calculate the total number of years worked in decimal form
    total_years = bartender_years + manager_years

    # Convert years to months and round to the nearest integer
    total_months = round(total_years * 12)

    result = total_months
    return result

print(solution())