def solution():
    """Uncle Jerry wants to reap ripe tomatoes from his garden. Yesterday, he was able to reap 120 tomatoes. Today, he was able to reap 50 more tomatoes than yesterday. How many tomatoes did Uncle Jerry reap?"""
    # Define the number of tomatoes reaped yesterday
    yesterday_tomatoes = 120

    # Calculate the number of tomatoes reaped today
    today_tomatoes = yesterday_tomatoes + 50

    # Calculate the total number of tomatoes reaped
    total_tomatoes = yesterday_tomatoes + today_tomatoes

    # return the result
    result = total_tomatoes
    return result

print(solution())