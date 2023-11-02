def solution():
    """Daniel owns a textile company. Every Monday he delivers 20 yards of fabric, and every Tuesday he delivers twice the amount of fabric he delivers on Monday. Every Wednesday, he delivers 1/4 of the amount of fabric he delivers on Tuesday. If each yard of fabric costs $2 and each yard of yarn costs $3, how much does he earn from Monday to Wednesday?"""
    yards_monday = 20
    yards_tuesday = 2 * yards_monday
    yards_wednesday = yards_tuesday / 4
    total_yards = yards_monday + yards_tuesday + yards_wednesday
    total_cost = 2 * total_yards
    result = total_cost
    return result

print(solution())