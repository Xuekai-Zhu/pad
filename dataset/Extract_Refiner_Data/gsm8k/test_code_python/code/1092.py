def solution():
    
    # Define the number of hours Billy can help per day
    HOURS_PER_DAY = 3

    # Define the number of days Billy has been helping
    DAYS_MON_FRI = 31

    # Define the number of people Billy can help per hour
    PEOPLE_PER_HOUR = 2

    # Calculate the total number of people Billy can help in a day
    total_people = HOURS_PER_DAY * PEOPLE_PER_HOUR * DAYS_MON_FRI

    # Calculate the number of days Billy has been helping for March 1st and April 19th
    days_between_1st_and_april = DAYS_MON_FRI / 0.2

    # Calculate the number of people Billy helps on the days between March 1st and April 19th
    people_on_other_days = total_people * (1 - days_between_1st_and_april) * 0.8

    # Display the number of people Billy helps

print(solution())