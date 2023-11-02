def solution():
    """Two days ago, Uncle Welly planted 50 roses on his vacant lot. Yesterday, he planted 20 more roses than the previous day. Today, he planted twice the number of roses than two days ago. How many roses did Uncle Welly plant in his vacant lot?"""
    two_days_ago = 50
    yesterday = two_days_ago + 20
    today = 2 * two_days_ago
    total_roses = two_days_ago + yesterday + today
    result = total_roses
    return result

print(solution())