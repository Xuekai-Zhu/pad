def solution():
    """Chris wants to hold his breath underwater for 90 straight seconds so he starts training each day. On the first day, he holds it for 10 seconds. On the second day, he holds it for 20 seconds. On the third day, he holds it for 30 seconds. After realizing that he can hold it for ten extra seconds each day, he realizes he can calculate how many days it is until he reaches 90 if he keeps up the same pace. So how many days until he can hold his breath for 90 seconds?"""
    # Define starting variables
    current_time = 0
    days = 3

    # Calculate how long Chris can hold his breath each day
    breath_increase = 10
    breath_time = 30
    while breath_time < 90:
        current_time += breath_time
        breath_time += breath_increase
        days += 1

    result = days
    return result

print(solution())