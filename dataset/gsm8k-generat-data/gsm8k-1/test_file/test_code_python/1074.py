def solution():
    """Melanie found a blueprint online for a toothpick sculpture she wanted to make. It requires 200 toothpicks. Melanie’s mom puts toothpicks in her sandwiches when she serves them for lunch. Melanie started saving them and has saved 10 toothpicks each week for the past 12 weeks. If she continues saving toothpicks at the same rate, how many more weeks will it take her to collect 200 toothpicks?"""
    total_toothpicks_needed = 200
    toothpicks_per_week = 10
    weeks_passed = 12
    current_toothpicks = toothpicks_per_week * weeks_passed
    toothpicks_remaining = total_toothpicks_needed - current_toothpicks
    weeks_needed = toothpicks_remaining / toothpicks_per_week
    result = weeks_needed
    return result

print(solution())