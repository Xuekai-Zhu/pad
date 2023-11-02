def solution():
    """Chris wants to hold his breath underwater for 90 straight seconds so he starts training each day. On the first day, he holds it for 10 seconds. On the second day, he holds it for 20 seconds. On the third day, he holds it for 30 seconds. After realizing that he can hold it for ten extra seconds each day, he realizes he can calculate how many days it is until he reaches 90 if he keeps up the same pace. So how many days until he can hold his breath for 90 seconds?"""
    # Define the initial holding time and the increment per day
    initial_time = 10
    increment = 10

    # Initialize the day counter and the total holding time
    day = 1
    total_time = initial_time

    # Increase the holding time and day counter until the total time reaches 90
    while total_time < 90:
        day += 1
        initial_time += increment
        total_time += initial_time

    result = day
    return result

print(solution())