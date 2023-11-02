def solution():
    """Jay has decided to save money from his paycheck every week. He has decided that he will increase the amount he saves each week by 10 dollars. If he started by saving 20 dollars this week, how much will he have saved in a month from now?"""
    initial_savings = 20
    weekly_increase = 10
    weeks_in_month = 4
    total_savings = initial_savings + ((weeks_in_month-1)*(initial_savings + weekly_increase*weeks_in_month)/2)
    result = total_savings
    return result

print(solution())