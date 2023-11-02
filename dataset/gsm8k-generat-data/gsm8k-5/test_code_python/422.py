def solution():
    total_hours = 8  # Bryan works 8 hours a day
    customer_outreach_hours = 4  # Bryan spends 4 hours on customer outreach posts
    advertisement_hours = customer_outreach_hours / 2  # Bryan spends half the time on advertisement posts

    # Calculate the total hours spent on marketing posts
    marketing_hours = total_hours - customer_outreach_hours - advertisement_hours
    result = marketing_hours
    return result

print(solution())