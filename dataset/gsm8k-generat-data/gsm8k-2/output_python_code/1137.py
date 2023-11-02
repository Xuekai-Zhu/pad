def solution():
    """Jay has decided to save money from his paycheck every week. He has decided that he will increase the amount he saves each week by 10 dollars. If he started by saving 20 dollars this week, how much will he have saved in a month from now?"""
    initial_save = 20
    weekly_increase = 10
    weeks_in_month = 4
    total_save = 0
    for week in range(weeks_in_month):
        total_save += initial_save + (week * weekly_increase)
    result = total_save
    return result

print(solution())