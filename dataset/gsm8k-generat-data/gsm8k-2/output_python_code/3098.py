def solution():
    """Natasha exercised for 30 minutes every day for one week. Esteban exercised for 10 minutes on each of nine days. How many hours did Natasha and Esteban exercise in total?"""
    natasha_minutes = 30 * 7
    esteban_minutes = 10 * 9
    total_minutes = natasha_minutes + esteban_minutes
    total_hours = total_minutes / 60
    result = total_hours
    return result

print(solution())