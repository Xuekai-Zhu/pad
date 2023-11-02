def solution():
    """Jason worked for 9 years as a bartender and 3 years and six months as a manager. How many months of work experience does he have total?"""
    # Define the number of years and months worked as a bartender and manager
    bartender_years = 9
    manager_years = 3
    manager_months = 6

    # Calculate the total number of months worked
    total_months = (bartender_years * 12) + (manager_years * 12) + manager_months

    # Display the total number of months worked
    result = total_months
    return result

print(solution())