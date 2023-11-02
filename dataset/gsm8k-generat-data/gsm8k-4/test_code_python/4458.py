def solution():
    """If the normal hours of operation of Jean's business are 4 pm to 10p every day Monday through Friday, and from 6 pm to 10 pm on weekends, how many hours is the business open in a week?"""
    # Define the number of hours the business is open Monday through Friday
    weekday_hours = (10 - 4) * 5

    # Define the number of hours the business is open on the weekend
    weekend_hours = (10 - 6) * 2

    # Calculate the total number of hours the business is open in a week
    total_hours = weekday_hours + weekend_hours

    # Return the result
    result = total_hours
    return result

print(solution())