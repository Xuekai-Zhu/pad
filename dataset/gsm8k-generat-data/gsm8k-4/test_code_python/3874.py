def solution():
    """Sara makes cakes during the five weekdays to sell on weekends. She makes 4 cakes a day and sells her cakes for $8. In 4 weeks she managed to sell all the cakes. How much money did she collect during that time?"""
    # Define the number of cakes Sara makes each day
    cakes_per_day = 4

    # Define the number of weekdays in a week
    weekdays_per_week = 5

    # Define the number of weeks
    weeks = 4

    # Calculate the total number of cakes Sara makes in 4 weeks
    total_cakes = cakes_per_day * weekdays_per_week * weeks

    # Calculate the total amount of money Sara collects by selling all the cakes
    total_money = total_cakes * 8

    result = total_money
    return result

print(solution())