def solution():
    """Sarah starts saving $5.00 a week for 4 weeks. Then she saves $10.00 a week for the next 4 weeks. Then she saves $20.00 a week for the next 4 weeks. How much money has she saved over 12 weeks?"""
    weeks_of_5 = 4
    weeks_of_10 = 4
    weeks_of_20 = 4
    amount_saved_5 = 5 * weeks_of_5
    amount_saved_10 = 10 * weeks_of_10
    amount_saved_20 = 20 * weeks_of_20
    total_saved = amount_saved_5 + amount_saved_10 + amount_saved_20
    result = total_saved
    return result

print(solution())