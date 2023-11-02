def solution():
    """Nancy takes 3 antacids per day when she eats Indian food, 2 antacids per day when she eats Mexican food, and 1 antacid per day otherwise. If Nancy eats Indian three times a week and Mexican twice a week, how many antacids does she take per month?"""
    indian_antacids = 3 * 7 * 3
    mexican_antacids = 2 * 7 * 2
    other_antacids = 1 * 7 * (30 - 3 - 2)
    total_antacids = indian_antacids + mexican_antacids + other_antacids
    result = total_antacids
    return result

print(solution())