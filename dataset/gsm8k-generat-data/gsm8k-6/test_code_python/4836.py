def solution():
    # Calculate the number of visits in a 30 day month
    total_visits = 50 * 24 * 30  # Jon gets 50 visits per hour and his website operates 24 hours a day and 30 days a month

    # Calculate the total amount earned in a 30 day month
    total_earned = total_visits * 0.10  # Jon gets paid $0.10 for each visit

    result = total_earned
    return result

print(solution())