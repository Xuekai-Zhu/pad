def solution():
    starting_amount = 20  # Jay starts by saving $20
    increase_per_week = 10  # Jay increases the amount he saves each week by $10
    weeks_in_month = 4  # There are 4 weeks in a month

    # Calculate the total amount Jay will have saved in a month
    total_amount_saved = starting_amount + (increase_per_week * (weeks_in_month - 1))  # Jay increases his savings for 3 weeks

    result = total_amount_saved
    return result

print(solution())