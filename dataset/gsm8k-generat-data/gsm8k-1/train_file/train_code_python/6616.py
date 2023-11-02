def solution():
    """Elsa and her sister watch an opera show every year at Central City Opera. Last year, opera seating cost $85 per ticket. This year, it costs $102. What is the percent increase in the cost of each ticket?"""
    old_price = 85
    new_price = 102
    percent_increase = ((new_price - old_price) / old_price) * 100
    result = percent_increase
    return result

print(solution())