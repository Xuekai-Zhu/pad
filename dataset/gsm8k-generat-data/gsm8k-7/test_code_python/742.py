def solution():
    initial_yards_cut = 8
    lawnmower_increase = 0.5  # 50% increase
    yards_cut_per_day = initial_yards_cut + (initial_yards_cut * lawnmower_increase)
    days = 7
    total_yards_cut = yards_cut_per_day * days
    result = total_yards_cut
    return result

print(solution())