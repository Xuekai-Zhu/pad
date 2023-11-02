def solution():
    """Uncle Jerry wants to reap ripe tomatoes from his garden. Yesterday, he was able to reap 120 tomatoes. Today, he was able to reap 50 more tomatoes than yesterday. How many tomatoes did Uncle Jerry reap?"""
    yesterday_tomatoes = 120
    today_tomatoes = yesterday_tomatoes + 50
    total_tomatoes = yesterday_tomatoes + today_tomatoes
    result = total_tomatoes
    return result

print(solution())