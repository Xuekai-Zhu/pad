def solution():
    """A factory produces 90 refrigerators per hour. It also produces 70 more coolers than refrigerators per hour. How many products did the factory produce for 5 days if it works 9 hours a day?"""
    # Define the number of refrigerators produced per hour and the number of coolers produced per hour
    REFRIGERATOR_PRODUCTION = 90
    COOLER_PRODUCTION = REFRIGERATOR_PRODUCTION + 70

    # Define the number of hours worked per day and the number of days worked
    HOURS_WORKED_PER_DAY = 9
    DAYS_WORKED = 5

    # Calculate the total number of products produced
    total_production = (REFRIGERATOR_PRODUCTION + COOLER_PRODUCTION) * HOURS_WORKED_PER_DAY * DAYS_WORKED

    # Display the total number of products produced
    result = total_production
    return result

print(solution())