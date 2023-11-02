def solution():
    """Sheena is sewing the bridesmaid’s dresses for her sister’s wedding. She can sew one dress in 12 hours. There are 5 bridesmaids in the wedding. If Sheena sews the dresses 4 hours each week, how many weeks will it take her to complete them?"""
    dresses_per_hour = 1/12
    total_dresses = 5
    hours_per_week = 4
    dresses_per_week = dresses_per_hour * hours_per_week
    total_weeks = total_dresses / dresses_per_week
    result = total_weeks
    return result

print(solution())