def solution():
    """Scott runs 3 miles every Monday through Wednesday. Then he runs twice as far he ran on Monday every Thursday and Friday. How many miles will he run in a month with 4 weeks?"""
    monday_wednesday_distance = 3 * 3  # 3 miles, 3 days a week
    thursday_friday_distance = 2 * (3 * 2)  # twice the distance on Monday, 2 days a week
    month_distance = (monday_wednesday_distance * 4 * 3) + (thursday_friday_distance * 4 * 2) # 4 weeks in a month
    result = month_distance
    return result

print(solution())