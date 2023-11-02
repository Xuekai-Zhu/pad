def solution():
    # Calculate the total number of visitors to Tim's website
    total_visitors = 100 * 6  # 100 visitors a day for the first 6 days
    last_day_visitors = 2 * total_visitors  # last day visitors were twice as many as the other days combined
    total_visitors += last_day_visitors  # add last day visitors to total visitors
    
    # Calculate the amount of money Tim made
    money_made = total_visitors * 0.01  # $.01 per visit
    result = money_made
    return result

print(solution())