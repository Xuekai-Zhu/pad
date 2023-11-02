def solution():
    """Sheena is sewing the bridesmaid’s dresses for her sister’s wedding. She can sew one dress in 12 hours. There are 5 bridesmaids in the wedding. If Sheena sews the dresses 4 hours each week, how many weeks will it take her to complete them?"""
    dress_time = 12
    num_bridesmaids = 5
    total_time = dress_time * num_bridesmaids
    hours_per_week = 4
    weeks_to_complete = total_time / hours_per_week
    result = weeks_to_complete
    return result

print(solution())