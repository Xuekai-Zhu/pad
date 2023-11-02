def solution():
    """If the normal hours of operation of Jean's business are 4 pm to 10 pm every day Monday through Friday, and from 6 pm to 10 pm on weekends, how many hours is the business open in a week?"""
    # Define the hours of operation for each day of the week
    weekday_hours = 6 # 4 pm to 10 pm = 6 hours
    weekend_hours = 4 # 6 pm to 10 pm = 4 hours

    # Calculate the total hours of operation for the week
    total_hours = (weekday_hours * 5) + (weekend_hours * 2)

    # Display the total hours of operation for the week
    result = total_hours
    return result

print(solution())