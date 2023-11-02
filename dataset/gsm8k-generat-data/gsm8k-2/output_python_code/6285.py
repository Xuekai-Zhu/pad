def solution():
    """3000 bees hatch from the queen's eggs every day. If a queen loses 900 bees every day, how many total bees are in the hive (including the queen) at the end of 7 days if at the beginning the queen had 12500 bees?"""
    queen_starting_bees = 12500
    daily_bee_hatch = 3000
    daily_bee_loss = 900
    total_bees = queen_starting_bees
    for i in range(1, 8):
        total_bees += daily_bee_hatch - daily_bee_loss
    result = total_bees
    return result

print(solution())