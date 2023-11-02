def solution():
    """Bryan works as a social media account manager. He does marketing posts, advertisement posts, and customer outreach posts. His client has him spend four hours on customer outreach posts and half that time on advertisement posts each day. Bryan works eight hours a day. How much time in hours each day does he spend on marketing posts?"""
    # Define the total number of hours worked by Bryan
    total_hours = 8

    # Define the number of hours spent on customer outreach posts
    outreach_hours = 4

    # Define the number of hours spent on advertisement posts
    ad_hours = outreach_hours / 2

    # Calculate the remaining time for marketing posts
    marketing_hours = total_hours - outreach_hours - ad_hours

    # return the result
    result = marketing_hours
    return result

print(solution())