def solution():
    """Kylie and Robert enjoy going to the beach to collect shells. On Monday, Kylie collects 5 more shells than Robert, who collects 20 shells. On Tuesday, Kylie collects 2 times more shells than she did on Monday. How many shells does Kylie collect on Tuesday?"""
    robert_shells = 20
    kylie_shells_monday = robert_shells + 5
    kylie_shells_tuesday = kylie_shells_monday * 2
    total_shells = kylie_shells_monday + kylie_shells_tuesday
    result = kylie_shells_tuesday
    return result

print(solution())