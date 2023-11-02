def solution():
    
    Monday_spending = 6
    Tuesday_spending = Monday_spending * 2
    Wednesday_spending = (Monday_spending + Tuesday_spending) * 2
    total_spending = Monday_spending + Tuesday_spending + Wednesday_spending
    result = total_spending
    return result

print(solution())