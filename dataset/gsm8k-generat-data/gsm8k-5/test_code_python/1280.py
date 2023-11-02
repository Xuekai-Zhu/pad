def solution():
    amount_earned = 80  # Honey earns $80 a day
    days_worked = 20  # Honey worked for 20 days
    total_earned = amount_earned * days_worked  # Honey earned $80 a day for 20 days

    amount_spent = 1360  # Honey spent $1360 in total
    amount_saved = total_earned - amount_spent  # Honey saved the rest of her pay

    result = amount_saved
    return result

print(solution())