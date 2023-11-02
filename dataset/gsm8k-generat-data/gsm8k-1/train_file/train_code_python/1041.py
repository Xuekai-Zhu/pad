def solution():
    """Kim's dad would buy her 2 candy bars a week. She would eat 1 candy bar every 4 weeks, saving the rest. After 16 weeks, how many candy bars did Kim have saved?"""
    candy_bars_per_week = 2
    candy_bars_eaten_per_cycle = 1
    cycles_to_save = 4
    weeks_to_save = cycles_to_save * (candy_bars_per_week - candy_bars_eaten_per_cycle)
    total_candy_bars_saved = weeks_to_save // cycles_to_save
    result = total_candy_bars_saved * 12  # 16 weeks / 4 weeks per cycle * 12 candy bars per year
    return result

print(solution())