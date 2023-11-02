def solution():
    """Jay has decided to save money from his paycheck every week. He has decided that he will increase the amount he saves each week by 10 dollars. If he started by saving 20 dollars this week, how much will he have saved in a month from now?"""
    # Define the initial amount saved and the increase per week
    initial_saved = 20
    increase_per_week = 10

    # Calculate the total amount saved in 4 weeks (1 month)
    total_saved = initial_saved + (initial_saved + increase_per_week) + (initial_saved + increase_per_week*2) + (initial_saved + increase_per_week*3)

    # Return the result
    result = total_saved
    return result

print(solution())