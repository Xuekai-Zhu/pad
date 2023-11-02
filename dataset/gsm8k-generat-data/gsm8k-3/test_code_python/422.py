def solution():
    """Bryan works as a social media account manager. He does marketing posts, advertisement posts, and customer outreach posts. His client has him spend four hours on customer outreach posts and half that time on advertisement posts each day. Bryan works eight hours a day. How much time in hours each day does he spend on marketing posts?"""
    # Define the total number of hours Bryan works each day
    TOTAL_HOURS = 8

    # Define the number of hours Bryan spends on customer outreach and advertisement posts
    CO_HOURS = 4
    AD_HOURS = CO_HOURS / 2

    # Calculate the number of hours Bryan spends on marketing posts
    MA_HOURS = TOTAL_HOURS - CO_HOURS - AD_HOURS

    # Display the number of hours Bryan spends on marketing posts
    result = MA_HOURS
    return result

print(solution())