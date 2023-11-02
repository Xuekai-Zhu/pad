def solution():
    """Daria is raising money for a new vacuum cleaner. So far, she has collected $20 in her piggy bank and has decided to put $10 in it each week. If the vacuum cleaner costs $120, how many weeks will it take her to raise enough money to cover this expense?"""
    starting_amount = 20
    weekly_contrib = 10
    vacuum_price = 120
    weeks_needed = (vacuum_price - starting_amount) / weekly_contrib
    result = weeks_needed
    return result

print(solution())