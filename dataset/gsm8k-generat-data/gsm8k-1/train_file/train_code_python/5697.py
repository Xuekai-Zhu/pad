def solution():
    """Daria is raising money for a new vacuum cleaner. So far, she has collected $20 in her piggy bank and has decided to put $10 in it each week. If the vacuum cleaner costs $120, how many weeks will it take her to raise enough money to cover this expense?"""
    initial_amount = 20
    weekly_contribution = 10
    vacuum_cleaner_cost = 120
    amount_left_to_raise = vacuum_cleaner_cost - initial_amount
    weeks_needed = amount_left_to_raise / weekly_contribution
    result = weeks_needed
    return result

print(solution())