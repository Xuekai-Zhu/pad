def solution():
    yesterday_tomatoes = 120  # Yesterday, Uncle Jerry was able to reap 120 tomatoes
    today_tomatoes = yesterday_tomatoes + 50  # Today, Uncle Jerry was able to reap 50 more tomatoes than yesterday

    # Calculate the total number of tomatoes Uncle Jerry reaped
    total_tomatoes = yesterday_tomatoes + today_tomatoes
    result = total_tomatoes
    return result

print(solution())