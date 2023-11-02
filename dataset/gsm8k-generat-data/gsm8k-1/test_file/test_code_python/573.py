def solution():
    """Mack wants to count things and decided to count how many birds there are in the sky over the next week. On days one and two, Mack saw a total of 50 birds. On day three he saw none. On days four and five, he saw 120 birds. On day six he saw 20 and on day seven he saw 90. On average, how many birds did Mack see in a day?"""
    total_birds = 50 + 0 + 120 + 20 + 90
    days_counted = 5
    average_birds_per_day = total_birds / days_counted
    result = average_birds_per_day
    return result

print(solution())