def solution():
    """Honey earned $80 a day. Every day, she spent part of her pay and saved the rest. After 20 days of work, she spent $1360. How much did Honey save in 20 days?"""
    total_earned = 80 * 20
    total_spent = 1360
    total_saved = total_earned - total_spent
    result = total_saved
    return result

print(solution())