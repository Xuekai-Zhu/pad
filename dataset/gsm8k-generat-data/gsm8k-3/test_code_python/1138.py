def solution():
    """Jay has decided to save money from his paycheck every week. He has decided that he will increase the amount he saves each week by 10 dollars. If he started by saving 20 dollars this week, how much will he have saved in a month from now?"""
    # Define the starting amount and the weekly increase
    start_amount = 20
    weekly_increase = 10

    # Calculate the total savings after a month (4 weeks)
    total_savings = sum([start_amount + (i * weekly_increase) for i in range(4)])

    # Display the total savings
    result = total_savings
    return result

print(solution())