def solution():
    """Bryan works as a social media account manager. He does marketing posts, advertisement posts, and customer outreach posts. His client has him spend four hours on customer outreach posts and half that time on advertisement posts each day. Bryan works eight hours a day. How much time in hours each day does he spend on marketing posts?"""
    total_hours = 8
    customer_outreach_time = 4
    advertisement_time = customer_outreach_time / 2
    marketing_time = total_hours - customer_outreach_time - advertisement_time
    result = marketing_time
    return result

print(solution())