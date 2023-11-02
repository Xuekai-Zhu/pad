def solution():
    """Terry spent 6$ for breakfast on Monday, twice as much on Tuesday, and on Wednesday Terry spent double what he did the previous two days combined. How much did Terry spend total?"""
    Monday_spending = 6
    Tuesday_spending = Monday_spending * 2
    Wednesday_spending = (Monday_spending + Tuesday_spending) * 2
    total_spending = Monday_spending + Tuesday_spending + Wednesday_spending
    result = total_spending
    return result

print(solution())