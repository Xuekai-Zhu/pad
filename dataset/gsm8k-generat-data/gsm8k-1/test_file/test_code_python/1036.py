def solution():
    """On Monday the post office delivered 425 letters. On Tuesday they delivered 17 more than one-fifth as many as Monday. On Wednesday they delivered 5 more than twice as many as they delivered on Tuesday. How many letters did the post office deliver Monday - Wednesday?"""
    monday_deliveries = 425
    tuesday_deliveries = 17 + (monday_deliveries // 5)
    wednesday_deliveries = 5 + (2 * tuesday_deliveries)
    total_deliveries = monday_deliveries + tuesday_deliveries + wednesday_deliveries
    result = total_deliveries
    return result

print(solution())