def solution():
    """Flora has been experiencing frequent fractures. Dr. Juan has asked her to strengthen her bones by drinking 105 gallons of milk within 3 weeks. Flora thinks that drinking 3 gallons of milk daily will be enough, but her brother says she'll still need to drink more. To fulfill Dr. Juan’s requirement, how many more gallons must Flora drink daily?"""
    # Define the total number of gallons Flora needs to drink
    TOTAL_GALLONS = 105

    # Define the number of weeks Flora has to drink the milk
    WEEKS = 3

    # Calculate the number of days Flora has to drink the milk
    DAYS = WEEKS * 7

    # Calculate the number of gallons Flora needs to drink daily to meet Dr. Juan's requirement
    daily_gallons_needed = TOTAL_GALLONS / DAYS

    # Calculate the additional gallons Flora needs to drink daily
    additional_gallons_needed = daily_gallons_needed - 3

    # Display the additional gallons Flora needs to drink daily
    result = additional_gallons_needed
    return result

print(solution())