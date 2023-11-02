def solution():
    """Droid owns a coffee shop. He uses 3 bags of coffee beans every morning, he uses triple that number in the afternoon than in the morning, and he uses twice the morning number in the evening. How many bags of coffee beans does he use every week?"""
    morning_beans = 3
    afternoon_beans = morning_beans * 3
    evening_beans = morning_beans * 2
    total_beans_per_day = morning_beans + afternoon_beans + evening_beans
    total_beans_per_week = total_beans_per_day * 7
    result = total_beans_per_week
    return result

print(solution())