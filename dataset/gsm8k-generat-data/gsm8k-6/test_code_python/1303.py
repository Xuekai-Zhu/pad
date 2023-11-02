def solution():
    monday_spending = 6  # Terry spent 6$ for breakfast on Monday
    tuesday_spending = 2 * monday_spending  # Terry spent twice as much on Tuesday
    wednesday_spending = (monday_spending + tuesday_spending) * 2  # Terry spent double what he did the previous two days combined on Wednesday
    total_spending = monday_spending + tuesday_spending + wednesday_spending  # Total spending
    result = total_spending
    return result

print(solution())