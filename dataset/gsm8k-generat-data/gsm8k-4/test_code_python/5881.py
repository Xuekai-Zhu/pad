def solution():
    """John's car gets 30 mpg. He drives 20 miles to work each way 5 days a week. He also drives another 40 miles a week for leisure travel. How many gallons of gas does he use a week?"""
    # Define the miles driven to work and for leisure
    work_miles = 20 * 2 * 5
    leisure_miles = 40

    # Calculate the total miles driven per week
    total_miles = work_miles + leisure_miles

    # Calculate the gallons of gas used per week
    gallons_used = total_miles / 30

    result = gallons_used
    return result

print(solution())