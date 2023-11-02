def solution():
    """Scott runs 3 miles every Monday through Wednesday. Then he runs twice as far he ran on Monday every Thursday and Friday. How many miles will he run in a month with 4 weeks?"""
    # Define the number of weeks in a month
    WEEKS_IN_MONTH = 4

    # Define the number of miles Scott runs on Monday through Wednesday
    MON_WED_MILES = 3

    # Calculate the number of miles Scott will run on Thursday and Friday
    THU_FRI_MILES = MON_WED_MILES * 2

    # Calculate the total miles Scott will run each week
    WEEKLY_MILES = (MON_WED_MILES * 3) + (THU_FRI_MILES * 2)

    # Calculate the total miles Scott will run in a month
    total_miles = WEEKLY_MILES * WEEKS_IN_MONTH

    # Display the total miles
    result = total_miles
    return result

print(solution())