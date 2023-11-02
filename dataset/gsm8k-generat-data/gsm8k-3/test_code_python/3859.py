def solution():
    """During the Christmas holidays, all shops are closed for 3 days. During each day during this time, a shop called "Surprise" could have earned 5 thousand dollars. How much potential revenue did the "Surprise" shop lose during 6 years of activity?"""
    # Define the number of days the shop is closed during the holidays
    days_closed = 3

    # Define the potential daily revenue loss
    daily_loss = 5000

    # Calculate the potential revenue loss during one year
    yearly_loss = days_closed * daily_loss

    # Calculate the potential revenue loss during 6 years
    total_loss = yearly_loss * 6

    # Display the potential revenue loss
    result = total_loss
    return result

print(solution())