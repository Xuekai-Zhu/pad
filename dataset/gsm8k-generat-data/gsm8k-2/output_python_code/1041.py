def solution():
    """Kim's dad would buy her 2 candy bars a week. She would eat 1 candy bar every 4 weeks, saving the rest. After 16 weeks, how many candy bars did Kim have saved?"""
    candy_bars_per_week = 2
    eaten_candy_bars_per_month = candy_bars_per_week / 4
    saved_candy_bars_per_month = candy_bars_per_week - eaten_candy_bars_per_month
    total_saved_candy_bars = saved_candy_bars_per_month * 4 * 16 - 1  # Subtract 1 for the candy bar she ate
    result = total_saved_candy_bars
    return result

print(solution())