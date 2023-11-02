def solution():
    """3000 bees hatch from the queen's eggs every day. If a queen loses 900 bees every day, how many total bees are in the hive (including the queen) at the end of 7 days if at the beginning the queen had 12500 bees?"""
    starting_bees = 12500
    daily_hatch = 3000
    daily_loss = 900
    total_bees = starting_bees + (daily_hatch - daily_loss) * 7
    result = total_bees
    return result

print(solution())