def solution():
    """John runs a telethon to raise money. For the first 12 hours, he generates $5000 per hour. The remaining 14 hours, he generates 20% more per hour. How much total money does he make?"""
    first_half_hours = 12
    second_half_hours = 14
    first_half_money = first_half_hours * 5000
    second_half_money = second_half_hours * 5000 * 1.2
    total_money = first_half_money + second_half_money
    result = total_money
    return result

print(solution())