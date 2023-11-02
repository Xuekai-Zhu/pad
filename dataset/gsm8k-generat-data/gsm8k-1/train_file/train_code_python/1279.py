def solution():
    """Honey earned $80 a day. Every day, she spent part of her pay and saved the rest. After 20 days of work, she spent $1360. How much did Honey save in 20 days?"""
    daily_pay = 80
    total_days = 20
    total_spent = 1360
    total_earned = daily_pay * total_days
    amount_saved = total_earned - total_spent
    result = amount_saved
    return result

print(solution())