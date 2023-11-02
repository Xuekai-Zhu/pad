def solution():
    """Scott runs 3 miles every Monday through Wednesday. Then he runs twice as far he ran on Monday every Thursday and Friday. How many miles will he run in a month with 4 weeks?"""
    # Define the number of miles ran on Monday
    monday_miles = 3

    # Define the total number of miles ran every Monday through Wednesday
    weekday_miles = 3 * 3

    # Define the number of miles ran on Thursday and Friday
    thur_fri_miles = monday_miles * 2

    # Define the total number of miles ran in a week
    weekly_miles = weekday_miles + thur_fri_miles

    # Define the total number of miles ran in a month
    monthly_miles = weekly_miles * 4

    # return the result
    result = monthly_miles
    return result

print(solution())