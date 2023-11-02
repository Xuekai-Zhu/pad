def solution():
    weekdays_trash = 8 * 6 * 250  # Monday to Saturday papers
    sunday_trash = 16 * 250  # Sunday paper
    total_trash = (weekdays_trash + sunday_trash) * 7 * 10  # 10 weeks worth of trash
    weight_in_ton = total_trash / 32000  # 32000 ounces in a ton
    earnings = weight_in_ton * 20  # $20 per ton
    result = earnings
    return result

print(solution())