def solution():
    """Mrs. Harrington bought 12 boxes of oranges at the market. She gave her mom and her sister 2 boxes of oranges each. Then she kept 1/4 of the oranges and sold the rest. How many oranges did Mrs. Harrington sell if each box contains 20 oranges?"""
    boxes_bought = 12
    boxes_given_away = 2 + 2
    boxes_kept = boxes_bought - boxes_given_away
    oranges_kept = boxes_kept * 20 * 0.25
    oranges_sold = boxes_kept * 20 - oranges_kept
    result = oranges_sold
    return result

print(solution())