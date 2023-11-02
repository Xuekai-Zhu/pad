def solution():
    total_oranges = 10 * 30  # There are 10 bags with 30 oranges each
    rotten_oranges = 50  # 50 pieces of oranges are rotten
    usable_oranges = total_oranges - rotten_oranges  # Usable oranges are total oranges minus rotten oranges
    juice_oranges = 30  # 30 pieces of oranges will be kept for making orange juice
    sold_oranges = usable_oranges - juice_oranges  # Sold oranges are usable oranges minus juice oranges
    result = sold_oranges
    return result

print(solution())